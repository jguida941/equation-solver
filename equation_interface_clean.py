from abc import ABC, abstractmethod

class Equation(ABC):
    """Abstract base class for equations."""

    degree: int

    def __init__(self, *args):
        pass

    def __init_subclass__(cls):
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