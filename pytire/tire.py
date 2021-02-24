"""
:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

import re
from .enums import Unit


class Tire:
    def __init__(self, size: str):
        self.size = size
        self._parse_units()

    def _parse_units(self) -> None:
        if re.match("\d{3}[xX]\d{3}-\d+", self.size): # noqa not an f-string
            self.unit = Unit.METRIC
        else:
            self.unit = Unit.IMPERIAL
