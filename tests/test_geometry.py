"""
Utility function unit tests

:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

import pytest

from pytire.enums import Unit
from pytire.geometry import circle_area, convert_length


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
