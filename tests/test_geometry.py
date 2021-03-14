"""
Utility function unit tests

:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

import math

import pytest

from pytire.enums import Unit
from pytire.geometry import (
    CiruclarToroid,
    Cuboid,
    Cylinder,
    NoneShape,
    SquareToroid,
    ThreeDimensionalShape,
    circle_area,
    convert_length,
    create_shape,
)


@pytest.mark.parametrize(
    ("length", "from_", "to_", "expected_result"),
    [
        (1, Unit.INCH, Unit.METRE, 0.0254),
        (50, Unit.INCH, Unit.METRE, 1.27),
        (-18, Unit.INCH, Unit.METRE, -0.4572),
        (1000, Unit.MILLIMETRE, Unit.METRE, 1),
        (1, Unit.METRE, Unit.METRE, 1),
    ],
)
def test_should_convert_lengths(length, expected_result, from_, to_):
    assert convert_length(length, from_unit=from_, to_unit=to_) == pytest.approx(
        expected_result
    )


@pytest.mark.parametrize(
    ("radius", "area"),
    [
        (1, 3.14159265358979),
        (5, 78.5398163397448),
    ],
)
def test_should_calculate_circular_area(radius, area):
    assert circle_area(radius) == pytest.approx(area)


@pytest.fixture
def cylinder():
    return Cylinder(outer_diameter=4, width=2, inner_diameter=3)


def test_cylinder_outer_radius(cylinder):
    assert cylinder.outer_radius == 2


def test_cylinder_volume(cylinder):
    assert cylinder.volume() == 8 * math.pi


@pytest.fixture
def cuboid():
    return Cuboid(outer_diameter=4, width=2, inner_diameter=3)


def test_cuboid_volume(cuboid):
    assert cuboid.volume() == 32


@pytest.fixture
def circular_toroid():
    return CiruclarToroid(outer_diameter=4, width=2, inner_diameter=3)


def test_circular_toroid_outer_radius(circular_toroid):
    assert circular_toroid.outer_radius == 2


def test_circular_toroid_inner_radius(circular_toroid):
    assert circular_toroid.inner_radius == 1.5


def test_circular_toroid_cross_section_radius(circular_toroid):
    assert circular_toroid.cross_section_radius == 0.25


def test_circular_toroid_swept_radius(circular_toroid):
    assert circular_toroid.swept_radius == 1.75


def test_circular_toroid_cross_sectional_area(circular_toroid):
    assert circular_toroid.cross_section_area() == 1 / 16 * math.pi


def test_circular_toroid_volume(circular_toroid):
    assert circular_toroid.volume() == math.pi ** 2 / 4 * (2 + 1.5) * (2 - 1.5) ** 2


@pytest.fixture
def square_toroid():
    return SquareToroid(outer_diameter=4, width=2, inner_diameter=3)


def test_square_toroid_volume(square_toroid):
    assert square_toroid.volume() == 7 / 2 * math.pi


def test_create_shape_success():
    shape = create_shape("cuboid", 1, 1, 1)
    assert isinstance(shape, ThreeDimensionalShape)


def test_create_shape_returns_none_shape():
    shape = create_shape("cuboid", None, None, None)
    assert isinstance(shape, NoneShape)


def test_create_shape_not_a_shape():
    with pytest.raises(ValueError):
        create_shape("hello", 1, 1, 1)
