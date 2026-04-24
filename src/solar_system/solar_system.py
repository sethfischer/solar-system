"""Solar System dimensions."""

from fractions import Fraction
from typing import Generator, Literal

from solar_system.constants import (
    DEFAULT_HELIOCENTRIC_DISTANCE_SCALE,
    DEFAULT_SCALE,
    EARTH_DIAMETER,
    EARTH_HELIOCENTRIC_DISTANCE,
    JUPITER_DIAMETER,
    JUPITER_HELIOCENTRIC_DISTANCE,
    KM_TO_MM,
    MARS_DIAMETER,
    MARS_HELIOCENTRIC_DISTANCE,
    MERCURY_DIAMETER,
    MERCURY_HELIOCENTRIC_DISTANCE,
    NEPTUNE_DIAMETER,
    NEPTUNE_HELIOCENTRIC_DISTANCE,
    SATURN_DIAMETER,
    SATURN_HELIOCENTRIC_DISTANCE,
    SUN_DIAMETER,
    SUN_HELIOCENTRIC_DISTANCE,
    URANUS_DIAMETER,
    URANUS_HELIOCENTRIC_DISTANCE,
    VENUS_DIAMETER,
    VENUS_HELIOCENTRIC_DISTANCE,
)


class Planet:
    """Planet."""

    def __init__(self, name: str, diameter_km: int, heliocentric_distance_km: int):
        """Initialise a planet."""
        self.name = name
        self.diameter_km = diameter_km
        self.heliocentric_distance_km = heliocentric_distance_km

    def scaled_diameter_mm(self, scale: Fraction) -> float:
        """Calculate scaled diameter in mm."""
        return self.diameter_km * scale * KM_TO_MM

    def scaled_heliocentric_distance_mm(self, scale: Fraction) -> float:
        """Calculate scaled distance from sun in mm."""
        return self.heliocentric_distance_km * scale * KM_TO_MM


class Star:
    """Star."""

    def __init__(self, name: str, diameter_km: int):
        """Initialise a star."""
        self.name = name
        self.diameter_km = diameter_km
        self.heliocentric_distance_km = SUN_HELIOCENTRIC_DISTANCE

    def scaled_diameter_mm(self, scale: Fraction) -> float:
        """Calculate scaled diameter in mm."""
        return self.diameter_km * scale * KM_TO_MM

    def scaled_heliocentric_distance_mm(self, scale: Fraction) -> float:
        """Calculate scaled distance from sun in mm."""
        return SUN_HELIOCENTRIC_DISTANCE * scale * KM_TO_MM


class SolarSystem:
    """Solar system."""

    def __init__(
        self,
        star: Star,
        scale: Fraction = DEFAULT_SCALE,
        heliocentric_distance_scale: Fraction = DEFAULT_HELIOCENTRIC_DISTANCE_SCALE,
    ):
        """Initialise a Solar System."""
        self._celestial_bodies: dict[str, Planet | Star] = {}

        self.add_celestial_body(star)
        self.scale = scale
        self.heliocentric_distance_scale = heliocentric_distance_scale

    def add_celestial_body(self, celestial_body: Planet | Star) -> Planet | Star:
        """Add an object to the system."""
        self._celestial_bodies[celestial_body.name.lower()] = celestial_body
        return celestial_body

    def get_celestial_body(self, name: str) -> Planet | Star:
        """Get an object by its name."""
        return self._celestial_bodies[name.lower()]

    def celestial_bodies(
        self, *, sort_by: Literal["distance"] = "distance"
    ) -> Generator[Planet | Star, None, None]:
        """Iterate over objects in the solar system, sorted by distance from sun."""
        sort_keys = {
            "distance": lambda p: p.heliocentric_distance_km,
        }
        celestial_bodies = iter(
            sorted(self._celestial_bodies.values(), key=sort_keys[sort_by])
        )

        yield from celestial_bodies

    def planets(self) -> Generator[Planet, None, None]:
        """Iterate over planets in the solar system."""
        for body in self._celestial_bodies.values():
            if isinstance(body, Planet):
                yield body

    def stars(self) -> Generator[Star, None, None]:
        """Iterate over stars in the solar system."""
        for body in self._celestial_bodies.values():
            if isinstance(body, Star):
                yield body


sun = Star("Sun", SUN_DIAMETER)
solar_system = SolarSystem(sun)
earth = Planet("Earth", EARTH_DIAMETER, EARTH_HELIOCENTRIC_DISTANCE)
solar_system.add_celestial_body(earth)
jupiter = Planet("Jupiter", JUPITER_DIAMETER, JUPITER_HELIOCENTRIC_DISTANCE)
solar_system.add_celestial_body(jupiter)
mars = Planet("Mars", MARS_DIAMETER, MARS_HELIOCENTRIC_DISTANCE)
solar_system.add_celestial_body(mars)
mercury = Planet("Mercury", MERCURY_DIAMETER, MERCURY_HELIOCENTRIC_DISTANCE)
solar_system.add_celestial_body(mercury)
neptune = Planet("Neptune", NEPTUNE_DIAMETER, NEPTUNE_HELIOCENTRIC_DISTANCE)
solar_system.add_celestial_body(neptune)
saturn = Planet("Saturn", SATURN_DIAMETER, SATURN_HELIOCENTRIC_DISTANCE)
solar_system.add_celestial_body(saturn)
uranus = Planet("Uranus", URANUS_DIAMETER, URANUS_HELIOCENTRIC_DISTANCE)
solar_system.add_celestial_body(uranus)
venus = Planet("Venus", VENUS_DIAMETER, VENUS_HELIOCENTRIC_DISTANCE)
solar_system.add_celestial_body(venus)
