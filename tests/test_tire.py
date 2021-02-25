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
