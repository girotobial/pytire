"""
Utility functions

:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

import abc
import math
from typing import Optional

from .constant import FEET_PER_METER, INCHES_PER_FOOT
from .enums import Unit


def convert_length(length: float, from_unit: Unit, to_unit: Unit) -> float:
    """Changes length measurements between units

    Parameters
    ----------
    length : float
        measurement to convert
    from_unit : Unit
        [description]
    to_unit : Unit
        [description]

    Returns
    -------
    float
        converted length in to_unit
    """

    if from_unit == to_unit:
        return length

    factors = {
        (Unit.INCH, Unit.METRE): 1.0 / (INCHES_PER_FOOT * FEET_PER_METER),
        (Unit.MILLIMETRE, Unit.METRE): 1 / 1000,
        (Unit.METRE, Unit.MILLIMETRE): 1000,
        (Unit.METRE, Unit.INCH): INCHES_PER_FOOT * FEET_PER_METER,
    }

    factor = factors.get((from_unit, to_unit))
    if factor is None:
        raise ValueError(
            f"Unable to provide conversion between {from_unit.name} and {to_unit.name}"
        )

    return length * factor


def circle_area(radius: float) -> float:
    """calculates the area of a circle

    Parameters
    ----------
    radius : float
        the radius of the circle

    Returns
    -------
    float
        the area of the circle
    """
    return radius ** 2 * math.pi


class ThreeDimensionalShape(abc.ABC):
    outer_diameter: float
    width: float
    innder_diameter: float

    @abc.abstractmethod
    def volume(self) -> float:
        pass


class Cylinder(ThreeDimensionalShape):
    def __init__(
        self,
        outer_diameter: float,
        width: float,
        inner_diameter: Optional[float] = None,
    ):
        self.outer_diameter = outer_diameter
        self.width = width
        self.inner_diameter = inner_diameter

    @property
    def outer_radius(self):
        return self.outer_diameter / 2

    def volume(self) -> float:
        return circle_area(self.outer_radius) * self.width


class Cuboid(ThreeDimensionalShape):
    def __init__(
        self,
        outer_diameter: float,
        width: float,
        inner_diameter: Optional[float] = None,
    ):
        self.outer_diameter = outer_diameter
        self.width = width
        self.inner_diameter = inner_diameter

    def volume(self) -> float:
        return self.outer_diameter * self.width


class CiruclarToroid(ThreeDimensionalShape):
    def __init__(self, outer_diameter: float, width: float, inner_diameter: float):
        self.outer_diameter = outer_diameter
        self.width = width
        self.innder_diameter = inner_diameter

    @property
    def outer_radius(self) -> float:
        return self.outer_diameter / 2.0

    @property
    def inner_radius(self) -> float:
        return self.innder_diameter / 2.0

    @property
    def cross_section_radius(self) -> float:
        return 0.5 * (self.outer_radius - self.inner_radius)

    def cross_section_area(self) -> float:
        return circle_area(self.cross_section_radius)

    @property
    def swept_radius(self) -> float:
        return self.outer_radius - self.cross_section_radius

    def volume(self) -> float:
        return 2 * math.pi * self.cross_section_area() * self.swept_radius


class SquareToroid(ThreeDimensionalShape):
    def __init__(self, outer_diameter: float, width: float, inner_diameter: float):
        self.outer_diameter = outer_diameter
        self.width = width
        self.innder_diameter = inner_diameter

        self.outer_cylinder = Cylinder(outer_diameter, width)
        self.inner_cylinder = Cylinder(inner_diameter, width)

    def volume(self) -> float:
        return self.outer_cylinder.volume() - self.inner_cylinder.volume()
