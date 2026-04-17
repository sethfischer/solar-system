"""Solar System console command."""

import csv
import locale
import sys
from argparse import ArgumentParser
from fractions import Fraction

from rich.console import Console
from rich.table import Table
from rich.text import Text
from typing_extensions import Literal

from solar_system import __version__
from solar_system.constants import KM_TO_MM, SUN_DIAMETER
from solar_system.solar_system import SolarSystem
from solar_system.solar_system import solar_system as _solar_system

locale.setlocale(locale.LC_ALL, "")


def format_fraction_colon(fraction: Fraction) -> str:
    """Format fraction with colon rather than a solidus."""
    return f"{fraction.numerator}:{fraction.denominator:,}"


def print_dimensions_pretty(solar_system: SolarSystem) -> int:
    """Print dimensions as a pretty table to stdout."""
    planet_scale_formatted = format_fraction_colon(solar_system.planet_scale)
    distance_from_sun_scale_formatted = format_fraction_colon(
        solar_system.distance_from_sun_scale
    )

    table = Table(title="Dimensions of Planets of the Solar System")
    table.add_column("Planet")
    table.add_column("Diameter\nkm")
    table.add_column("Distance from Sun\nkm")
    table.add_column(f"Model diameter\n{planet_scale_formatted}\nmm")
    table.add_column(
        f"Model distance from sun\n{distance_from_sun_scale_formatted}\nmm"
    )

    for planet in solar_system.planets.values():
        scaled_distance_from_sun = planet.scaled_distance_from_sun_mm(
            solar_system.distance_from_sun_scale
        )
        table.add_row(
            planet.name,
            "{:n}".format(planet.diameter_km),
            "{:n}".format(planet.distance_from_sun_km),
            f"{planet.scaled_diameter_mm(solar_system.planet_scale):,.1f}",
            f"{scaled_distance_from_sun:,.1f}",
        )

    console = Console()
    console.print(table)

    scaled_sun_diameter = SUN_DIAMETER * solar_system.planet_scale * KM_TO_MM
    sun_scale_note = Text(
        f"Note: At a scale of {planet_scale_formatted} "
        f"the Sun diameter is {scaled_sun_diameter:,.1f} mm."
    )
    console.print(sun_scale_note)

    return 0


def print_dimensions_csv(solar_system: SolarSystem) -> int:
    """Print dimensions table as CSV to stdout."""
    planet_scale_formatted = format_fraction_colon(solar_system.planet_scale)
    distance_from_sun_scale_formatted = format_fraction_colon(
        solar_system.distance_from_sun_scale
    )

    writer = csv.writer(sys.stdout)
    writer.writerow(
        [
            "Planet",
            "Diameter (km)",
            "Distance from Sun (km)",
            f"Model diameter {planet_scale_formatted} (mm)",
            f"Model distance from sun {distance_from_sun_scale_formatted} (mm)",
        ]
    )

    for planet in solar_system.planets.values():
        scaled_distance_from_sun = planet.scaled_distance_from_sun_mm(
            solar_system.distance_from_sun_scale
        )
        writer.writerow(
            [
                planet.name,
                planet.diameter_km,
                planet.distance_from_sun_km,
                f"{planet.scaled_diameter_mm(solar_system.planet_scale):.1f}",
                f"{scaled_distance_from_sun:.1f}",
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

    return parser


def main() -> int:
    """Solar System console command."""
    parser = build_parser()

    if len(sys.argv) == 1:
        parser.print_help()
        return 0

    args = parser.parse_args()

    if args.command == "dimensions":
        return print_dimensions(_solar_system, args.data_format)

    return 0


if __name__ == "__main__":
    main()
