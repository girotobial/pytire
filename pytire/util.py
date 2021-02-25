"""
Utility functions

:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

from .constant import FEET_PER_METER, INCHES_PER_FOOT


def convert_inches_to_meters(inches: float) -> float:
    """Changes inches into meters

    Parameters
    ----------
    inches : float
        A length in inches

    Returns
    -------
    float
        A length in meters
    """

    return inches / (INCHES_PER_FOOT * FEET_PER_METER)
