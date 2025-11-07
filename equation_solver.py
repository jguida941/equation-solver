# ================= CODE EXPLANATION =================
# FCC: FreeCodeCamp.org
# Python: Learn Interfaces by Building an Equation Solver
# https://www.freecodecamp.org/learn/scientific-computing-with-python/learn-interfaces-by-building-an-equation-solver/step-1
"""This gives extra commentary and explanation for the code in the exercises."""

# ================= IMPORTS =================
from abc import ABC, abstractmethod

# ================= INTERFACE DEFINITION =================
# Python doesn't have a native `interface` keyword.
# Using an abstract base class (ABC) defines a contract that subclasses must fulfill.
# ABC stands for "Abstract Base Class", it lets you create abstract methods.
# You import it from the abc module using: from abc import ABC.
# This allows you to import a specific class from a module.

class Equation(ABC):  # Make sure to inherit from ABC
    """Contract: subclasses must implement solve() and analyze()."""

    # An interface (abstract base class) can also define regular methods
    # that are inherited by concrete classes.
    # A concrete class is one that can be instantiated
    # (i.e., you can actually create objects from it).
    def __init__(self):
        pass  # placeholder so the file runs

    # @abstractmethod marks a method that has no implementation here.
    # It forces any subclass to write its own version.
    # Think of it like a "must-do" checklist for child classes.

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
    # Implementing the abstract methods from Equation.
    # Do NOT use @abstractmethod here, subclasses must provide
    # real implementations so the class can be instantiated.

    def solve(self):
        """Compute and return the solution."""
        pass  # placeholder so the file runs

    def analyze(self):
        """Return quick facts (e.g., {'type': 'linear'})."""
        pass  # placeholder


# ================= INSTANCES =================
# lin_eq = LinearEquation()  # commented out: must implement all abstract methods
# eq = Equation()  # commented out: abstract classes cannot be instantiated directly
