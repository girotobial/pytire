"""
:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

from typing import Optional

from pytire.size import get_size


class Tire:
    """A rubber pneumatic tire.

    Attributes
    ----------
    size : str
        Size code as would be displayed on the sidewall.
        E.g 'H45.5x16.5-21', '30x10.75-16', '615x225-10'
    """

    def __init__(self, size: str):
        """A rubber pneumatic tire.

        Parameters
        ----------
        size : str
            Size code as would be displayed on the sidewall.
            E.g 'H45.5x16.5-21', '30x10.75-16', '615x225-10'
        """
        self._size = get_size(size_string=size)

    @property
    def size(self) -> str:
        return self._size.__str__()

    @property
    def outer_diameter(self) -> Optional[float]:
        """Tire diameter in metres"""
        return self._size.outer_diameter

    @property
    def width(self) -> Optional[float]:
        """Tire width in metres"""
        return self._size.width

    @property
    def rim_diameter(self) -> Optional[float]:
        """Wheel diameter in metres"""
        return self._size.rim_diameter

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

        return self._size.volume(geometry=geometry)

    @property
    def aspect_ratio(self) -> Optional[float]:
        """The ratio between the height of the tyre's sidewall to its width.

        Returns
        -------
        Optional[float]
            The aspect ratio to 3 decimal places.
        """
        return self._size.aspect_ratio
