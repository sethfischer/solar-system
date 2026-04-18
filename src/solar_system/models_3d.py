"""Planet models."""

from typing import Literal

import cadquery as cq

from solar_system.cq_containers import CqWorkplaneContainer


class DualHemispherePlanet3DModel(CqWorkplaneContainer):
    """Models a planet as two hemispheres."""

    _cq_object: cq.Workplane

    def __init__(
        self, diameter: float, hemisphere: Literal["lower", "upper"] = "upper"
    ) -> None:
        """Initialise a planet."""
        self.diameter = diameter
        self.hemisphere = hemisphere

        self._cq_object = self._make()

    def _make(self) -> cq.Workplane:
        """Make planet."""
        if self.diameter >= 15:
            planet = self._make_large_planet()
        else:
            planet = self._make_small_planet()

        if self.hemisphere == "upper":
            hemisphere = planet.split(keepTop=True)
        else:
            hemisphere = planet.split(keepBottom=True)
            # rotate to print with planer side on print bed
            hemisphere = hemisphere.rotate((0, 0, 0), (1, 0, 0), 180)

        return hemisphere

    @staticmethod
    def make_mounting_pin_cut_pattern() -> cq.Workplane:
        """Mounting pin cut pattern."""
        mounting_pin_diameter = 2
        mounting_pin_length = 50
        clearance = 0.25

        return (
            cq.Workplane()
            .cylinder(mounting_pin_length, (mounting_pin_diameter + clearance) / 2)
            .translate((0, 0, -(mounting_pin_length / 2)))
        )

    @staticmethod
    def make_locating_pin_cut_pattern() -> cq.Workplane:
        """Locating pin cut pattern."""
        locating_pin_diameter = 1.75  # filament diameter
        locating_pin_length = 20
        locating_pin_length_clearance = 2  # assembly clearance
        locating_pin_diameter_clearance = 0.3

        diameter = locating_pin_diameter + locating_pin_diameter_clearance
        length = locating_pin_length + locating_pin_length_clearance

        return cq.Workplane().cylinder(length, diameter / 2)

    def _make_large_planet(self) -> cq.Workplane:
        """3D model of a large planet.

        A large planet consists of two hemispheres joined by a central locating
        pin. The mounting pin protrudes part way through the lower hemisphere.
        """
        # recession of mounting pin into lower hemisphere in mm
        mounting_pin_recession = 10

        planet = cq.Workplane().sphere(self.diameter / 2)
        locating_pin = self.make_locating_pin_cut_pattern()
        planet = planet.cut(locating_pin)

        mounting_pin = self.make_mounting_pin_cut_pattern()
        planet = planet.cut(
            mounting_pin.translate(
                (0, 0, -(self.diameter / 2) + mounting_pin_recession)
            )
        )

        return planet

    def _make_small_planet(self) -> cq.Workplane:
        """3D model of a small planet.

        A small planet consists of two hemispheres with the mounting pin
        extending through the lower hemisphere into the upper hemisphere.
        """
        # protrusion of mounting pin into upper hemisphere as
        # ratio of planet radius
        mounting_pin_protrusion = 0.5

        planet = cq.Workplane().sphere(self.diameter / 2)
        mounting_pin = self.make_mounting_pin_cut_pattern()
        planet = planet.cut(
            mounting_pin.translate(
                (0, 0, (self.diameter / 2) * mounting_pin_protrusion)
            )
        )

        return planet

    @property
    def cq_object(self) -> cq.Workplane:
        """Get CadQuery object."""
        return self._cq_object
