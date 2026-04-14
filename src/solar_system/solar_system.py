"""Solar System dimensions."""

from fractions import Fraction

from solar_system.constants import (
    DEFAULT_DISTANCE_FROM_SUN_SCALE,
    DEFAULT_PLANET_SCALE,
    EARTH_DIAMETER,
    EARTH_DISTANCE_FROM_SUN,
    JUPITER_DIAMETER,
    JUPITER_DISTANCE_FROM_SUN,
    KM_TO_MM,
    MARS_DIAMETER,
    MARS_DISTANCE_FROM_SUN,
    MERCURY_DIAMETER,
    MERCURY_DISTANCE_FROM_SUN,
    NEPTUNE_DIAMETER,
    NEPTUNE_DISTANCE_FROM_SUN,
    SATURN_DIAMETER,
    SATURN_DISTANCE_FROM_SUN,
    URANUS_DIAMETER,
    URANUS_DISTANCE_FROM_SUN,
    VENUS_DIAMETER,
    VENUS_DISTANCE_FROM_SUN,
)


class Planet:
    """Planet."""

    def __init__(self, name: str, diameter_km: int, distance_from_sun_km: int):
        """Initialise a planet."""
        self.name = name
        self.diameter_km = diameter_km
        self.distance_from_sun_km = distance_from_sun_km

    def scaled_diameter_mm(self, scale: Fraction) -> float:
        """Calculate scaled diameter of planet in mm."""
        return self.diameter_km * scale * KM_TO_MM

    def scaled_distance_from_sun_mm(self, scale: Fraction) -> float:
        """Calculate scaled distance from sun in mm."""
        return self.distance_from_sun_km * scale * KM_TO_MM


class SolarSystem:
    """Solar system."""

    planets: dict[str, Planet] = {}

    def __init__(
        self,
        planet_scale: Fraction = DEFAULT_PLANET_SCALE,
        distance_from_sun_scale: Fraction = DEFAULT_DISTANCE_FROM_SUN_SCALE,
    ):
        """Initialise a Solar System."""
        self.planet_scale = planet_scale
        self.distance_from_sun_scale = distance_from_sun_scale

    def add_planet(self, planet: Planet) -> Planet:
        """Add a planet to the system."""
        self.planets[planet.name.lower()] = planet
        return planet

    def get_planet(self, name: str) -> Planet:
        """Get a planet by its name."""
        return self.planets[name.lower()]


solar_system = SolarSystem()
earth = Planet("Earth", EARTH_DIAMETER, EARTH_DISTANCE_FROM_SUN)
solar_system.add_planet(earth)
jupiter = Planet("Jupiter", JUPITER_DIAMETER, JUPITER_DISTANCE_FROM_SUN)
solar_system.add_planet(jupiter)
mars = Planet("Mars", MARS_DIAMETER, MARS_DISTANCE_FROM_SUN)
solar_system.add_planet(mars)
mercury = Planet("Mercury", MERCURY_DIAMETER, MERCURY_DISTANCE_FROM_SUN)
solar_system.add_planet(mercury)
neptune = Planet("Neptune", NEPTUNE_DIAMETER, NEPTUNE_DISTANCE_FROM_SUN)
solar_system.add_planet(neptune)
saturn = Planet("Saturn", SATURN_DIAMETER, SATURN_DISTANCE_FROM_SUN)
solar_system.add_planet(saturn)
uranus = Planet("Uranus", URANUS_DIAMETER, URANUS_DISTANCE_FROM_SUN)
solar_system.add_planet(uranus)
venus = Planet("Venus", VENUS_DIAMETER, VENUS_DISTANCE_FROM_SUN)
solar_system.add_planet(venus)
