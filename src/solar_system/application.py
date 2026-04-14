"""Solar System console command."""

import locale
from argparse import ArgumentParser
from fractions import Fraction

from rich.console import Console
from rich.table import Table
from rich.text import Text

from solar_system import __version__
from solar_system.constants import KM_TO_MM, SUN_DIAMETER
from solar_system.solar_system import SolarSystem
from solar_system.solar_system import solar_system as _solar_system

locale.setlocale(locale.LC_ALL, "")


def format_fraction_colon(fraction: Fraction) -> str:
    """Format fraction with colon."""
    return f"{fraction.numerator}:{fraction.denominator:,}"


def build_parser() -> ArgumentParser:
    """Parse arguments."""
    parser = ArgumentParser(
        prog="solar_system", description="Solar System console command."
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    return parser


def dimensions_table(solar_system: SolarSystem) -> None:
    """Print dimensions table."""
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


def main() -> int:
    """Solar System console command."""
    parser = build_parser()
    args = parser.parse_args()

    try:
        func = args.func
        func(args)  # noqa
    except AttributeError:
        dimensions_table(_solar_system)

    return 0


if __name__ == "__main__":
    main()
