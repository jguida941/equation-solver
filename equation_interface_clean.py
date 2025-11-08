from abc import ABC, abstractmethod

class Equation(ABC):
    """Abstract base class for equations."""

    degree: int

    def __init__(self, *args):
        """Make sure number of args matches degree + 1."""
        if len(args) != self.degree + 1:
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )

        """Ensure all args are int or float."""
        if any (not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")

        """Check for highest degree coefficient not being zero"""
        if args[0] == 0:
            raise ValueError('Highest degree coefficient must be different from zero')

    def __init_subclass__(cls):
        """Ensure subclasses define the 'degree' attribute."""
        if not hasattr(cls, "degree"):
            raise AttributeError(f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'")

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

lin_eq = LinearEquation(2,3)
