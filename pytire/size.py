import abc
import re
from typing import Optional

from pytire.constant import DIAMETER_RE, METRIC_RE, WHEEL_DIAMETER_RE, WIDTH_RE
from pytire.enums import Unit
from pytire.geometry import ThreeDimensionalShape, convert_length, create_shape


class Size(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, size: str):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def outer_diameter(self) -> Optional[float]:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def width(self) -> Optional[float]:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def rim_diameter(self) -> Optional[float]:
        raise NotImplementedError

    def volume(self, geometry: str = "cuboid") -> Optional[float]:
        """The exterior volume of the tire.

        Parameters
        ----------
        geometry : str, default 'cuboid'
            The shape assumed during the calculation of the volume.
            allowed values are ['cuboid', 'cylinder', 'square_toroid', 'torus']

        Returns
        -------
        float
            Volume in m^2
        """
        shape: ThreeDimensionalShape = create_shape(
            geometry, self.outer_diameter, self.width, self.rim_diameter
        )
        return shape.volume()

    @property
    @abc.abstractmethod
    def aspect_ratio(self) -> Optional[float]:
        raise NotImplementedError

    @abc.abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError


class AircraftSize(Size):
    def __init__(self, size: str):
        self._size = size
        self.unit = Unit.MILLIMETRE if re.match(METRIC_RE, self._size) else Unit.INCH

    def __str__(self) -> str:
        return self._size

    @property
    def outer_diameter(self) -> Optional[float]:
        match = re.search(DIAMETER_RE, self._size)
        if match is None:
            return match

        outer_diameter = float(match.group(0))
        return convert_length(outer_diameter, self.unit, Unit.METRE)

    @property
    def width(self) -> Optional[float]:
        """Size width in metres"""

        match = re.search(WIDTH_RE, self._size)
        if match is None:
            return match

        width = float(match.group(0))
        return convert_length(width, self.unit, Unit.METRE)

    @property
    def rim_diameter(self) -> Optional[float]:
        """Rim diameter in metres"""

        match = re.search(WHEEL_DIAMETER_RE, self._size)
        if match is None:
            return match

        wheel_diameter = float(match.group(0))
        return convert_length(wheel_diameter, Unit.INCH, Unit.METRE)

    @property
    def aspect_ratio(self) -> Optional[float]:
        """The ratio between the height of the tyre's sidewall to its width.

        Returns
        -------
        Optional[float]
            The aspect ratio to 3 decimal places.
        """
        if (
            self.outer_diameter is None
            or self.width is None
            or self.rim_diameter is None
        ):
            return None

        numerator = 0.5 * (self.outer_diameter - self.rim_diameter)

        return round(numerator / self.width, 3)


def get_size(size_string: str) -> Size:
    return AircraftSize(size_string)
