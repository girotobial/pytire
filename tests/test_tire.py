"""
:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

import pytest
from pytire import Tire


@pytest.mark.parametrize(
    "size",
    [
        "H30x9.50-16",
        "27x7.75-15",
        "615x225-10",
        "18X5.5",
        "12.50-16",
    ]
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
        ("615x225-10", 0.615, 0.225, 0.10),
        ("18X5.5", 0.4572, 0.1397, None),
        ("12.50-16", None, 0.3175, 0.4064),
    ]
)
def test_should_set_attributes(size, diameter, width, wheel_diameter):
    tire = Tire(size)
    assert tire.diameter == diameter
    assert tire.width == width
    assert tire.wheel_diameter == wheel_diameter
