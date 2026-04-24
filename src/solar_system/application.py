"""Solar System console command."""

import csv
import locale
import logging
import sys
from argparse import ArgumentParser
from fractions import Fraction
from pathlib import Path

from rich.console import Console
from rich.table import Table
from typing_extensions import Literal

from solar_system import __version__
from solar_system.models_3d import DualHemispherePlanet3DModel
from solar_system.solar_system import SolarSystem
from solar_system.solar_system import solar_system as _solar_system

logger = logging.getLogger(__name__)

locale.setlocale(locale.LC_ALL, "")


def format_fraction(
    fraction: Fraction, seperator: str = ":", exponential: bool = False
) -> str:
    """Format fraction."""
    if exponential:
        return f"{fraction.numerator:}{seperator}{fraction.denominator:.0e}"

    return f"{fraction.numerator}{seperator}{fraction.denominator:,}"


def print_dimensions_pretty(solar_system: SolarSystem) -> int:
    """Print dimensions as a pretty table to stdout."""
    scale_formatted = format_fraction(solar_system.scale)
    heliocentric_distance_scale_formatted = format_fraction(
        solar_system.heliocentric_distance_scale
    )

    table = Table(title="Objects of the Solar System")
    table.add_column("Name")
    table.add_column("Diameter\nkm")
    table.add_column("Distance from Sun\nkm")
    table.add_column(f"Model diameter\n{scale_formatted}\nmm")
    table.add_column(
        f"Model distance from sun\n{heliocentric_distance_scale_formatted}\nmm"
    )

    for celestial_body in solar_system.celestial_bodies():
        scaled_heliocentric_distance = celestial_body.scaled_heliocentric_distance_mm(
            solar_system.heliocentric_distance_scale
        )
        table.add_row(
            celestial_body.name,
            "{:n}".format(celestial_body.diameter_km),
            "{:n}".format(celestial_body.heliocentric_distance_km),
            f"{celestial_body.scaled_diameter_mm(solar_system.scale):,.1f}",
            f"{scaled_heliocentric_distance:,.1f}",
        )

    console = Console()
    console.print(table)

    return 0


def print_dimensions_csv(solar_system: SolarSystem) -> int:
    """Print dimensions table as CSV to stdout."""
    scale_formatted = format_fraction(solar_system.scale)
    heliocentric_distance_scale_formatted = format_fraction(
        solar_system.heliocentric_distance_scale
    )

    writer = csv.writer(sys.stdout)
    writer.writerow(
        [
            "Name",
            "Diameter (km)",
            "Distance from Sun (km)",
            f"Model diameter {scale_formatted} (mm)",
            f"Model distance from sun {heliocentric_distance_scale_formatted} (mm)",
        ]
    )

    for celestial_body in solar_system.celestial_bodies():
        scaled_heliocentric_distance = celestial_body.scaled_heliocentric_distance_mm(
            solar_system.heliocentric_distance_scale
        )
        writer.writerow(
            [
                celestial_body.name,
                celestial_body.diameter_km,
                celestial_body.heliocentric_distance_km,
                f"{celestial_body.scaled_diameter_mm(solar_system.scale):.1f}",
                f"{scaled_heliocentric_distance:.1f}",
            ]
        )

    return 0


def print_dimensions(
    solar_system: SolarSystem, data_format: Literal["csv", "pretty"]
) -> int:
    """Print dimensions to stdout using specified formatter."""
    if data_format == "csv":
        return print_dimensions_csv(solar_system)

    # default is to print a pretty table
    return print_dimensions_pretty(solar_system)


def build_planets(solar_system: SolarSystem, output_directory: Path) -> int:
    """Export planet components in 3D model format."""
    hemispheres: list[Literal["lower", "upper"]] = ["lower", "upper"]
    scale_exponential = format_fraction(
        solar_system.scale, seperator="-", exponential=True
    )
    for planet in solar_system.planets():
        for hemisphere in hemispheres:
            path_name = (
                output_directory
                / f"{planet.name.lower()}_{hemisphere}_{scale_exponential}.stl"
            )
            logger.info(f"Exporting {path_name}")

            planet_hemisphere = DualHemispherePlanet3DModel(
                planet.scaled_diameter_mm(solar_system.scale),
                hemisphere=hemisphere,
            )
            planet_hemisphere.cq_object.export(path_name.as_posix())

    return 0


def build_parser() -> ArgumentParser:
    """Parse arguments."""
    parser = ArgumentParser(
        prog="solar_system",
        description="Solar System console command.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command")

    dimensions_subparser = subparsers.add_parser(
        "dimensions", help="Show the dimensions of the solar system"
    )
    dimensions_subparser.add_argument(
        "-f",
        "--format",
        dest="data_format",
        choices=["csv", "pretty"],
        default="pretty",
        help="Output data format: 'csv' or 'pretty' (default: pretty)",
    )

    build_subparser = subparsers.add_parser(
        "build",
        help="Build files for 3D printing",
    )
    build_subparser.add_argument(
        "-o",
        "--output-directory",
        metavar="DIR",
        type=Path,
        default=Path("./_build"),
        help="Directory for built files (default: _build)",
    )

    return parser


def main() -> int:
    """Solar System console command."""
    logging.basicConfig(level=logging.INFO)

    parser = build_parser()

    if len(sys.argv) == 1:
        parser.print_help()
        return 0

    args = parser.parse_args()

    if args.command == "dimensions":
        return print_dimensions(_solar_system, args.data_format)

    if args.command == "build":
        return build_planets(_solar_system, args.output_directory)

    return 0


if __name__ == "__main__":
    main()
