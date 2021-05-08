"""
:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

import pytest

from pytire.enums import Unit
from pytire.size import AircraftSize, Size


@pytest.mark.unit
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
def test_should_construct_aircraft_size(size):
    size_instance = AircraftSize(size)
    assert isinstance(size_instance, Size)


@pytest.mark.unit
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
    size_instance = AircraftSize(size)
    assert size_instance.unit == expected_unit


@pytest.mark.integration
@pytest.mark.parametrize(
    ("size", "expected_value"),
    [
        ("H30x9.50-16", 0.1401093972),
        ("27x7.75-15", 0.09258281483),
        ("615x225-10", 0.085100625),
        ("12.50-16", None),
        ("18X5.5", 0.02920174805),
        ("H44.5x16.5-21", 0.5354329775),
    ],
)
def test_should_calculate_cuboid_volume(size, expected_value):
    size = AircraftSize(size)
    assert size.volume(geometry="cuboid") == pytest.approx(expected_value)


@pytest.mark.integration
@pytest.mark.parametrize(
    ("size", "expected_value"),
    [
        ("H30x9.50-16", 0.110041652671605),
        ("27x7.75-15", 0.0727143657522103),
        ("615x225-10", 0.066837874578975),
        ("12.50-16", None),
        ("18X5.5", 0.0229349970831344),
        ("H44.5x16.5-21", 0.420528036795157),
    ],
)
def test_should_calculate_cylinder_volume(size, expected_value):
    size = AircraftSize(size)
    assert size.volume(geometry="cylinder") == pytest.approx(expected_value)
