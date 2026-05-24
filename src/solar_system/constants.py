"""Constants."""

from fractions import Fraction

#########################
# Unit conversion factors
#########################

KM_TO_MM = 1e6

#############################
# Default 3D print parameters
#############################

FILAMENT_DIAMETER = 1.75
DEFAULT_EXTRUSION_WIDTH_DEFAULT = 0.44
DEFAULT_EXTRUSION_WIDTH_EXTERNAL_PERIMETER = 0.42


################
# Default scales
################

# one : one billion one hundred and fifty million
DEFAULT_SCALE = Fraction(1, 1_150_000_000)
# one : five trillion
DEFAULT_HCO_SCALE = Fraction(1, 5_000_000_000_000)


#####################################
# Default star slice dimensions in mm
#####################################

DEFAULT_STAR_SLICE_LENGTH = 100
DEFAULT_STAR_SLICE_THICKNESS = 65
DEFAULT_STAR_SLICE_HEIGHT = 200


#########################
# Planet dimensions in km
#########################

SUN_DIAMETER = 1_391_400
SUN_HCO = 0

EARTH_DIAMETER = 12_756
EARTH_HCO = 149_600_000

JUPITER_DIAMETER = 142_984
JUPITER_HCO = 778_500_000

MARS_DIAMETER = 6_792
MARS_HCO = 227_900_000

MERCURY_DIAMETER = 4_879
MERCURY_HCO = 57_900_000

NEPTUNE_DIAMETER = 49_528
NEPTUNE_HCO = 4_495_100_000

SATURN_DIAMETER = 120_536
SATURN_HCO = 1_443_500_000

URANUS_DIAMETER = 51_118
URANUS_HCO = 2_872_500_000

VENUS_DIAMETER = 12_104
VENUS_HCO = 108_200_000
