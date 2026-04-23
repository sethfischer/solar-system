"""Solar System dimensions."""

from fractions import Fraction

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
        """Calculate scaled diameter of planet in mm."""
        return self.diameter_km * scale * KM_TO_MM

    def scaled_heliocentric_distance_mm(self, scale: Fraction) -> float:
        """Calculate scaled distance from sun in mm."""
        return self.heliocentric_distance_km * scale * KM_TO_MM


class SolarSystem:
    """Solar system."""

    planets: dict[str, Planet] = {}

    def __init__(
        self,
        scale: Fraction = DEFAULT_SCALE,
        heliocentric_distance_scale: Fraction = DEFAULT_HELIOCENTRIC_DISTANCE_SCALE,
    ):
        """Initialise a Solar System."""
        self.scale = scale
        self.heliocentric_distance_scale = heliocentric_distance_scale

    def add_planet(self, planet: Planet) -> Planet:
        """Add a planet to the system."""
        self.planets[planet.name.lower()] = planet
        return planet

    def get_planet(self, name: str) -> Planet:
        """Get a planet by its name."""
        return self.planets[name.lower()]


solar_system = SolarSystem()
earth = Planet("Earth", EARTH_DIAMETER, EARTH_HELIOCENTRIC_DISTANCE)
solar_system.add_planet(earth)
jupiter = Planet("Jupiter", JUPITER_DIAMETER, JUPITER_HELIOCENTRIC_DISTANCE)
solar_system.add_planet(jupiter)
mars = Planet("Mars", MARS_DIAMETER, MARS_HELIOCENTRIC_DISTANCE)
solar_system.add_planet(mars)
mercury = Planet("Mercury", MERCURY_DIAMETER, MERCURY_HELIOCENTRIC_DISTANCE)
solar_system.add_planet(mercury)
neptune = Planet("Neptune", NEPTUNE_DIAMETER, NEPTUNE_HELIOCENTRIC_DISTANCE)
solar_system.add_planet(neptune)
saturn = Planet("Saturn", SATURN_DIAMETER, SATURN_HELIOCENTRIC_DISTANCE)
solar_system.add_planet(saturn)
uranus = Planet("Uranus", URANUS_DIAMETER, URANUS_HELIOCENTRIC_DISTANCE)
solar_system.add_planet(uranus)
venus = Planet("Venus", VENUS_DIAMETER, VENUS_HELIOCENTRIC_DISTANCE)
solar_system.add_planet(venus)
