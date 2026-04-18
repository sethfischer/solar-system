"""Abstract base classes for CadQuery object containers."""

from abc import ABC, abstractmethod

import cadquery as cq


class CqWorkplaneContainer(ABC):
    """Abstract base class for CadQuery Workplane containers."""

    _cq_object: cq.Workplane

    @property
    def cq_object(self) -> cq.Workplane:
        """Get CadQuery object."""
        return self._cq_object

    @abstractmethod
    def _make(self) -> cq.Workplane:
        """Create CadQuery object."""
        ...
