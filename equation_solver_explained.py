# ================= CODE EXPLANATION =================

# FCC: FreeCodeCamp.org
# Python: Learn Interfaces by Building an Equation Solver
# https://www.freecodecamp.org/learn/scientific-computing-with-python/learn-interfaces-by-building-an-equation-solver/step-1
"""This gives extra commentary and explanation for the code in the exercises."""

# ================= IMPORTS =================
from abc import ABC, abstractmethod


# ================= INTERFACE DEFINITION =================

# Python doesn't have a native `interface` keyword
# Using an abstract base class (ABC) defines a contract that subclasses must fulfill
# ABC stands for "Abstract Base Class", it lets you create abstract methods
# You import it from the abc module using: from abc import ABC
# This allows you to import a specific class from a module

class Equation(ABC):  # Make sure to inherit from ABC
    """Contract: subclasses must implement solve() and analyze()."""

    # Annotate a variable to indicate its type.
    # Python recognizes data types at runtime, but type hints
    # help other developers understand what kind of data is expected.
    degree: int

    # An interface (abstract base class) can also define regular methods
    # that are inherited by concrete classes
    # A concrete class is one that can be instantiated
    # (meaning you can actually create objects from it)

    def __init__(self, *args):  # You need be able to pass a variable number of arguments
                                # We use args and * to accept any # of positional arguments

        # A linear equation (degree 1) has 2 coefficients:
        # one for x¹ (e.g., 4 in 4x) and one for x⁰ (the constant term, e.g., 5)
        # Example: 4x + 5 = 0  →  LinearEquation(4, 5)
        # So we must check that the number of arguments matches degree + 1
        if len(args) != self.degree + 1:
            raise ValueError (f"'{self.__class__.__name__}' object takes {self.degree + 1} positional arguments but {len(args)} were given")


    # Advanced: this special method is called automatically
    # whenever a subclass of this class is created.
    # It allows customization or tracking of subclass behavior.
    # 'cls' refers to the new subclass being defined.
    def __init_subclass__(cls):
        # hasattr returns a boolean indicating if the class has the specified attribute
        # we are looking for the 'degree' attribute
        if not hasattr(cls, 'degree'):
            # AttributeError warns the developer that they forgot to define 'degree'
            raise AttributeError(f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'")

    # @abstractmethod marks a method that has no implementation here
    # It forces any subclass to write its own version
    # Think of it like a "must-do" checklist for child classes
    @abstractmethod
    def solve(self):
        """Compute and return the solution."""
        pass  # placeholder so the file runs

    @abstractmethod
    def analyze(self):
        """Return quick facts (e.g., {'type': 'linear'})."""
        pass  # placeholder


# ================= SUBCLASS EXAMPLE =================

class LinearEquation(Equation):
    """Concrete class representing a linear equation."""

    # You assign degree = 1 in the LinearEquation subclass because
    # it represents a first-degree (linear) equation.
    # Linear equation → highest power of x is 1 → degree = 1
    degree: int = 1

    # Implementing the abstract methods from Equation
    # Do NOT use @abstractmethod here, subclasses must provide
    # real implementations so the class can be instantiated
    def solve(self):
        """Compute and return the solution."""
        pass  # placeholder so the file runs

    def analyze(self):
        """Return quick facts (e.g., {'type': 'linear'})."""
        pass  # placeholder

# ================= INSTANCES =================

# lin_eq = LinearEquation()  # commented out: must implement all abstract methods
# eq = Equation()  # commented out: abstract classes cannot be instantiated directly