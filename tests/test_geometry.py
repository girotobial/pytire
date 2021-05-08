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
    Cuboid,
    Cylinder,
    NoneShape,
    SquareToroid,
    ThreeDimensionalShape,
    Torus,
    circle_area,
    convert_length,
    create_shape,
)


@pytest.mark.unit
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


@pytest.mark.unit
def test_should_fail_to_convert():
    class FakeUnit:
        name = "fake"

    with pytest.raises(ValueError):
        convert_length(1, FakeUnit, Unit.METRE)


@pytest.mark.unit
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
    return Cylinder(diameter=4, width=2)


@pytest.mark.unit
def test_cylinder_radius(cylinder):
    assert cylinder.radius == 2


@pytest.mark.unit
def test_cylinder_volume(cylinder):
    assert cylinder.volume() == 8 * math.pi


@pytest.fixture
def cuboid():
    return Cuboid(height=4, length=4, width=2)


@pytest.mark.unit
def test_cuboid_volume(cuboid):
    assert cuboid.volume() == 32


@pytest.mark.unit
def test_cuboid_from_tyre():
    cuboid = Cuboid.from_tire_dimensions(4, 3, 2)
    assert cuboid.height == 4
    assert cuboid.length == 4
    assert cuboid.width == 3


@pytest.fixture
def torus():
    return Torus(radius_of_revolution=1.75, cross_section_radius=0.25)


@pytest.mark.unit
def test_should_be_invalid_torus():
    with pytest.raises(TypeError):
        Torus(None, None)


@pytest.mark.unit
def test_torus_cross_sectional_area(torus):
    assert torus.cross_section_area() == 1 / 16 * math.pi


@pytest.mark.unit
def test_torus_volume(torus):
    assert torus.volume() == math.pi ** 2 / 4 * (2 + 1.5) * (2 - 1.5) ** 2


@pytest.fixture
def square_toroid():
    return SquareToroid(outer_diameter=4, width=2, inner_diameter=3)


@pytest.mark.unit
def test_square_toroid_volume(square_toroid):
    assert square_toroid.volume() == 7 / 2 * math.pi


@pytest.mark.unit
def test_none_shape_constructor():
    NoneShape.from_tire_dimensions(0, 0, 0)


@pytest.mark.unit
def test_none_shape_volume():
    assert NoneShape().volume() is None


@pytest.mark.unit
def test_create_shape_success():
    shape = create_shape("cuboid", 1, 1, 1)
    assert isinstance(shape, ThreeDimensionalShape)


@pytest.mark.unit
def test_create_shape_returns_none_shape():
    shape = create_shape("cuboid", None, None, None)
    assert isinstance(shape, NoneShape)


@pytest.mark.unit
def test_create_shape_not_a_shape():
    with pytest.raises(ValueError):
        create_shape("hello", 1, 1, 1)
