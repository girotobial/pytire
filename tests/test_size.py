"""
:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

import pytest

from pytire.enums import Unit
from pytire.size import AircraftSize, RoadSize, Size, get_size

# AircraftTire tests


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
def test_should_return_size_string():
    SIZE_STRING = "34x10.75-16"
    size_instance = AircraftSize(SIZE_STRING)
    assert str(size_instance) == SIZE_STRING


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


# RoadSize tests
@pytest.fixture
def roadsize_str() -> str:
    return "205/55R16"


@pytest.fixture
def roadsize(roadsize_str) -> RoadSize:
    return RoadSize(roadsize_str)


@pytest.mark.unit
def test_should_construct_roadsize(roadsize_str):
    tire = RoadSize(roadsize)
    assert isinstance(tire, RoadSize)


@pytest.mark.unit
def test_should_return_roadsize_outer_diameter(roadsize):
    assert roadsize.outer_diameter == pytest.approx(0.315)


def test_should_return_roadsize_rim_diameter(roadsize):
    assert roadsize.rim_diameter == pytest.approx(0.4064)


@pytest.mark.unit
def test_should_return_roadsize_width(roadsize):
    assert roadsize.width == pytest.approx(0.205)


@pytest.mark.unit
def test_should_return_roadsize_aspect_ratio(roadsize):
    assert roadsize.aspect_ratio == pytest.approx(0.65)


# get_size tests
@pytest.mark.unit
@pytest.mark.parametrize(
    ("size_string", "expected_instance"),
    [
        ("H30x9.50-16", AircraftSize),
        ("27x7.75-15", AircraftSize),
        ("615x225-10", AircraftSize),
        ("615x225R10", AircraftSize),
        ("12.50-16", AircraftSize),
        ("18X5.5", AircraftSize),
        ("H44.5x16.5-21", AircraftSize),
        ("H44.5x16.5R21", AircraftSize),
        ("205/55R16", RoadSize),
    ],
)
def test_should_return_instance(size_string, expected_instance):
    size = get_size(size_string)
    assert isinstance(size, expected_instance)
