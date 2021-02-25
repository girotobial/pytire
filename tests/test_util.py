"""
Utility function unit tests

:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

import pytest

from pytire.util import convert_inches_to_meters


@pytest.mark.parametrize(
    ("inches", "meters"), [(1, 0.0254), (50, 1.27), (-18, -0.4572)]
)
def test_should_convert_to_meters(inches, meters):
    assert convert_inches_to_meters(inches) == pytest.approx(meters)
