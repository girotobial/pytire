"""
Utility functions

:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

from __future__ import annotations

import abc
import math
from typing import Optional

from pytire.constant import FEET_PER_METER, INCHES_PER_FOOT
from pytire.enums import Unit


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
    """Defines the interface for 3D shapes."""

    @abc.abstractmethod
    def volume(self) -> Optional[float]:
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def from_tire_dimensions(
        cls, outer_diameter: float, width: float, inner_diameter: float
    ) -> ThreeDimensionalShape:
        raise NotImplementedError


class Cylinder(ThreeDimensionalShape):
    """A right angled cylinder.

    Parameters
    ----------
    diameter : float
        the length of the straight line that passes through the center of the circular cross section
    width : float
        The length of the side orthagonol to the circular cross section
    """

    def __init__(
        self,
        diameter: float,
        width: float,
    ):
        """A right angled cylinder.

        Parameters
        ----------
        diameter : float
            the length of the straight line that passes through the center of the circular cross section
        width : float
            The length of the side orthagonol to the circular cross section
        """
        self.diameter = diameter
        self.width = width
        self._validate_args()

    def _validate_args(
        self,
    ) -> None:
        args = {
            "diameter": self.diameter,
            "width": self.width,
        }
        if None in args.values():
            raise TypeError(
                f"Cannot create {self.__class__} with {args} as one or more is None"
            )

    @property
    def radius(self):
        return self.diameter / 2

    def volume(self) -> float:
        return circle_area(self.radius) * self.width

    @classmethod
    def from_tire_dimensions(
        cls, outer_diameter: float, width: float, inner_diameter: float
    ) -> Cylinder:
        return cls(outer_diameter, width)


class Cuboid(ThreeDimensionalShape):
    """A rectangular cuboid

    Parameters
    ----------
    height : float

    length : float

    width : float

    """

    def __init__(
        self,
        height: float,
        length: float,
        width: float,
    ):
        """A rectangular cuboid

        Parameters
        ----------
        height : float
            the height of the cuboid
        length : float
            the length of the cuboid
        width : float
            the width of the cuboid
        """
        self.height = height
        self.length = length
        self.width = width
        self._validate_args()

    def _validate_args(
        self,
    ) -> None:
        args = {
            "length": self.length,
            "height": self.height,
            "width": self.width,
        }
        if None in args.values():
            raise TypeError(
                f"Cannot create {self.__class__} with {args} as one or more is None"
            )

    def volume(self) -> float:
        """the volume of the cuboid"""
        return self.height * self.width * self.length

    @classmethod
    def from_tire_dimensions(
        cls, outer_diameter: float, width: float, inner_diameter: float
    ) -> Cuboid:
        return cls(outer_diameter, outer_diameter, width)


class CiruclarToroid(ThreeDimensionalShape):
    def __init__(self, outer_diameter: float, width: float, inner_diameter: float):
        self.outer_diameter: float = outer_diameter
        self.width: float = width
        self.inner_diameter: float = inner_diameter
        self._validate_args()

    def _validate_args(
        self,
    ) -> None:
        args = {
            "outer_diameter": self.outer_diameter,
            "width": self.width,
            "inner_diameter": self.inner_diameter,
        }
        if None in args.values():
            raise TypeError(
                f"Cannot create {self.__class__} with {args} as one or more is None"
            )

    @property
    def outer_radius(self) -> float:
        return self.outer_diameter / 2.0

    @property
    def inner_radius(self) -> float:
        return self.inner_diameter / 2.0

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

    @classmethod
    def from_tire_dimensions(
        cls, outer_diameter: float, width: float, inner_diameter: float
    ) -> CiruclarToroid:
        return cls(outer_diameter, width, inner_diameter)


class SquareToroid(ThreeDimensionalShape):
    def __init__(self, outer_diameter: float, width: float, inner_diameter: float):
        self.outer_diameter = outer_diameter
        self.width = width
        self.inner_diameter = inner_diameter
        self._validate_args()

    def _validate_args(
        self,
    ) -> None:
        args = {
            "outer_diameter": self.outer_diameter,
            "width": self.width,
            "inner_diameter": self.inner_diameter,
        }
        if None in args.values():
            raise TypeError(
                f"Cannot create {self.__class__} with {args} as one or more is None"
            )

    def volume(self) -> float:
        outer_cylinder = Cylinder(self.outer_diameter, self.width)
        inner_cylinder = Cylinder(self.inner_diameter, self.width)
        return outer_cylinder.volume() - inner_cylinder.volume()

    @classmethod
    def from_tire_dimensions(
        cls, outer_diameter: float, width: float, inner_diameter: float
    ) -> SquareToroid:
        return cls(outer_diameter, width, inner_diameter)


class NoneShape(ThreeDimensionalShape):
    def __init__(
        self,
    ):
        pass

    def volume(self) -> None:
        return None

    @classmethod
    def from_tire_dimensions(
        cls, outer_diameter: float, width: float, inner_diameter: float
    ):
        return cls()


def create_shape(
    geometry: str,
    outer_diameter: Optional[float],
    width: Optional[float],
    inner_diameter: Optional[float],
) -> ThreeDimensionalShape:
    _shapes = {
        "cuboid": Cuboid,
        "cylinder": Cylinder,
        "square_toroid": SquareToroid,
        "circular_toroid": CiruclarToroid,
    }

    try:
        shape = _shapes[geometry].from_tire_dimensions(  # type:ignore
            outer_diameter, width, inner_diameter
        )
    except TypeError:
        shape = NoneShape()
    except KeyError:
        raise ValueError(
            f"{geometry} is not an available shape please select one of {list(_shapes.keys())}"
        )

    return shape
