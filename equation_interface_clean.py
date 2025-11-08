from abc import ABC, abstractmethod

class Equation(ABC):
    """Abstract base class for equations."""

    degree: int

    def __init__(self, *args):
        """Make sure number of args matches degree + 1."""
        if len(args) != self.degree + 1:
            raise ValueError(f"'{self.__class__.__name__}' object takes {self.degree + 1} positional arguments but {len(args)} were given")

    def __init_subclass__(cls):
        """Ensure subclasses define the 'degree' attribute."""
        if not hasattr(cls, "degree"):
            raise AttributeError(f"Subclass '{cls.__name__}' missing required 'degree' attribute")

    @abstractmethod
    def solve(self):
        pass

    @abstractmethod
    def analyze(self):
        pass


class LinearEquation(Equation):
    """Concrete class for a linear equation (degree = 1)."""

    degree = 1

    def solve(self):
        pass

    def analyze(self):
        pass