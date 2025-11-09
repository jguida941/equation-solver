from abc import ABC, abstractmethod

class Equation(ABC):
    """Abstract base class for equations."""

    degree: int

    def __init__(self, *args):
        # Verify argument count
        if len(args) != self.degree + 1:
            raise TypeError(
                f"'{self.__class__.__name__}' object takes {self.degree + 1} positional arguments "
                f"but {len(args)} were given"
            )

        # Validate coefficient types
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")

        # Ensure leading coefficient is nonzero
        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")

        # Store coefficients as {degree: value}
        self.coefficients = {len(args) - 1 - i: arg for i, arg in enumerate(args)}

    def __init_subclass__(cls):
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )

    def __str__(self):
        terms = []
        # join terms to form equation string
        equation_string = ' '.join(terms)
        return equation_string

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


lin_eq = LinearEquation(2, 3)
print(lin_eq)