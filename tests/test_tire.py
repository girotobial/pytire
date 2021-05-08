"""
:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

import pytest

from pytire import Tire


@pytest.mark.integration
@pytest.mark.parametrize(
    ("size", "diameter", "width", "wheel_diameter"),
    [
        ("H30x9.50-16", 0.762, 0.2413, 0.4064),
        ("27x7.75-15", 0.6858, 0.19685, 0.381),
        ("615x225-10", 0.615, 0.225, 0.254),
        ("18X5.5", 0.4572, 0.1397, None),
        ("12.50-16", None, 0.3175, 0.4064),
        ("H44.5x16.5-21", 1.1303, 0.4191, 0.5334),
        ("-20", None, None, 0.507999984),
    ],
)
def test_should_set_attributes(size, diameter, width, wheel_diameter):
    tire = Tire(size)
    assert tire.outer_diameter == pytest.approx(diameter)
    assert tire.width == pytest.approx(width)
    assert tire.rim_diameter == pytest.approx(wheel_diameter)


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
    tire = Tire(size)
    assert tire.volume(geometry="cylinder") == pytest.approx(expected_value)


@pytest.mark.integration
@pytest.mark.parametrize(
    ("size", "expected_value"),
    [
        ("H30x9.50-16", 0.0455685047567235),
        ("27x7.75-15", 0.0305676926318393),
        ("615x225-10", 0.034928823917073),
        ("12.50-16", None),
        ("18X5.5", None),
        ("H44.5x16.5-21", 0.182821765999277),
    ],
)
def test_should_calculate_torus_volume(size, expected_value):
    tire = Tire(size)
    assert tire.volume(geometry="torus") == pytest.approx(expected_value)


@pytest.mark.integration
@pytest.mark.parametrize(
    ("size", "expected_value"),
    [
        ("H30x9.50-16", 0.0787409159116815),
        ("27x7.75-15", 0.050271660273133),
        ("615x225-10", 0.05543695702894),
        ("12.50-16", None),
        ("18X5.5", None),
        ("H44.5x16.5-21", 0.326876798705692),
    ],
)
def test_should_calculate_square_toroid_volume(size, expected_value):
    tire = Tire(size)
    assert tire.volume(geometry="square_toroid") == pytest.approx(expected_value)


@pytest.mark.integration
@pytest.mark.parametrize(
    ("size", "expected_value"),
    [
        ("H30x9.50-16", 0.737),
        ("27x7.75-15", 0.774),
        ("615x225-10", 0.802),
        ("12.50-16", None),
        ("18X5.5", None),
        ("H44.5x16.5-21", 0.712),
    ],
)
def test_should_calculate_aspect_ratio(size, expected_value):
    tire = Tire(size)
    assert tire.aspect_ratio == pytest.approx(expected_value)
