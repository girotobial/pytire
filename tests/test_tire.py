"""
:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

import pytest

from pytire import Tire
from pytire.enums import Unit


@pytest.mark.parametrize(
    "size",
    [
        "H30x9.50-16",
        "27x7.75-15",
        "615x225-10",
        "18X5.5",
        "12.50-16",
        "H44.5x16.5-21",
    ],
)
def test_should_call_successfully(size):
    tire = Tire(size)
    assert isinstance(tire, Tire)
    assert tire.size == size


@pytest.mark.parametrize(
    ("size", "diameter", "width", "wheel_diameter"),
    [
        ("H30x9.50-16", 0.762, 0.2413, 0.4064),
        ("27x7.75-15", 0.6858, 0.19685, 0.381),
        ("615x225-10", 0.615, 0.225, 0.254),
        ("18X5.5", 0.4572, 0.1397, None),
        ("12.50-16", None, 0.3175, 0.4064),
        ("H44.5x16.5-21", 1.1303, 0.4191, 0.5334),
    ],
)
def test_should_set_attributes(size, diameter, width, wheel_diameter):
    tire = Tire(size)
    assert tire.diameter == pytest.approx(diameter)
    assert tire.width == pytest.approx(width)
    assert tire.wheel_diameter == pytest.approx(wheel_diameter)


@pytest.mark.parametrize(
    ("size", "expected_unit"),
    [
        ("H30x9.50-16", Unit.INCH),
        ("27x7.75-15", Unit.INCH),
        ("615x225-10", Unit.MILLIMETRE),
        ("18X5.5", Unit.INCH),
        ("12.50-16", Unit.INCH),
        ("H44.5x16.5-21", Unit.INCH),
    ],
)
def test_should_detect_correct_unit(size, expected_unit):
    tire = Tire(size)
    assert tire.unit == expected_unit


@pytest.mark.parametrize(
    ("size", "expected_value"),
    [
        ("H30x9.50-16", 0.184),
        ("27x7.75-15", 0.135),
        ("615x225-10", 0.138),
        ("12.50-16", None),
        ("18X5.5", 0.064),
        ("H44.5x16.5-21", 0.474),
    ],
)
def test_should_calculate_cuboid_volume(size, expected_value):
    tire = Tire(size)
    assert tire.volume(geometry="cuboid") == pytest.approx(expected_value)


@pytest.mark.parametrize(
    ("size", "expected_value"),
    [
        ("H30x9.50-16", 0.110),
        ("27x7.75-15", 0.073),
        ("615x225-10", 0.067),
        ("12.50-16", None),
        ("18X5.5", 0.023),
        ("H44.5x16.5-21", 0.421),
    ],
)
def test_should_calculate_cylinder_volume(size, expected_value):
    tire = Tire(size)
    assert tire.volume(geometry="cylinder", center_hole_filled=True) == pytest.approx(
        expected_value
    )


@pytest.mark.parametrize(
    ("size", "expected_value"),
    [
        ("H30x9.50-16", 0.110),
        ("27x7.75-15", 0.073),
        ("615x225-10", 0.067),
        ("12.50-16", None),
        ("18X5.5", 0.023),
        ("H44.5x16.5-21", 0.421),
    ],
)
def test_should_calculate_circular_toroid_volume(size, expected_value):
    tire = Tire(size)
    assert tire.volume(geometry="circular_toroid") == pytest.approx(expected_value)


@pytest.mark.parametrize(
    ("size", "expected_value"),
    [
        ("H30x9.50-16", 0.0456),
        ("27x7.75-15", 0.0306),
        ("615x225-10", 0.0349),
        ("12.50-16", None),
        ("18X5.5", None),
        ("H44.5x16.5-21", 0.1828),
    ],
)
def test_should_calculate_square_toroid_volume(size, expected_value):
    tire = Tire(size)
    assert tire.volume(geometry="square_toroid") == pytest.approx(expected_value)
