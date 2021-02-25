"""
:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

import re
from typing import Optional

from .constant import DIAMETER_RE, METRIC_RE, WHEEL_DIAMETER_RE, WIDTH_RE
from .enums import Unit
from .util import convert_inches_to_meters


class Tire:
    def __init__(self, size: str):
        self.size = size
        self.unit = Unit.METRIC if re.match(METRIC_RE, self.size) else Unit.IMPERIAL

    @property
    def diameter(self) -> Optional[float]:
        """Tire diameter in metres"""

        match = re.search(DIAMETER_RE, self.size)

        if match is None:
            return match

        diameter = float(match.group(0))
        if self.unit == Unit.IMPERIAL:
            return convert_inches_to_meters(diameter)

        if self.unit == Unit.METRIC:
            return diameter / 1000

        return None

    @property
    def width(self) -> Optional[float]:
        """Tire width in metres"""

        match = re.search(WIDTH_RE, self.size)
        if match is None:
            return match

        width = float(match.group(0))

        if self.unit == Unit.IMPERIAL:
            return convert_inches_to_meters(width)

        if self.unit == Unit.METRIC:
            return width / 1000
        return None

    @property
    def wheel_diameter(self) -> Optional[float]:
        """Wheel diameter in metres"""

        match = re.search(WHEEL_DIAMETER_RE, self.size)
        if match is None:
            return match

        wheel_diameter = float(match.group(0))
        return convert_inches_to_meters(wheel_diameter)
