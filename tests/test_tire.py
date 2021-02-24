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
