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


    # ==================== TYPE ANNOTATION =================

    # Annotate a variable to indicate its type.
    # Python recognizes data types at runtime, but type hints
    # help other developers understand what kind of data is expected.

    degree: int


    # ==================== INIT METHOD =================

    # An interface (abstract base class) can also define regular methods
    # that are inherited by concrete classes
    # A concrete class is one that can be instantiated
    # (meaning you can actually create objects from it)

    def __init__(self, *args):  # You need be able to pass a variable number of arguments
                                # We use args and * to accept any # of positional arguments


        # ================= CHECK ARGUMENT COUNT =================

        # A linear equation (degree 1) has 2 coefficients:
        # one for x¹ (e.g., 4 in 4x) and one for x⁰ (the constant term, e.g., 5)
        # Example: 4x + 5 = 0  →  LinearEquation(4, 5)
        # So we must check that the number of arguments matches degree + 1

        if len(args) != self.degree + 1:

            # ================= RAISE TYPE ERROR =================

            # A TypeError indicates that the function received an argument of the wrong type
            raise (TypeError
                   (f"'{self.__class__.__name__}' object takes {self.degree + 1} "f"positional arguments but {len(args)} were given"))


        # ================= CHECK DEGREE TYPE =================

        # isinstance() takes 2 arguments and returns a boolean (True or False)
        # It checks if the first argument is an instance of the second argument (a class or tuple of classes)
        # Example:
        # x = 5
        # isinstance(x, int)   → True
        # isinstance(x, str)   → False
        # isinstance(LinearEquation(2, 3), Equation) → True

        # Ensure degree is an integer
        if not isinstance(self.degree, int):
            raise TypeError(f"'degree' attribute must be of type int, got {type(self.degree).__name__}")

        # Ensure all passed coefficients are numeric
        for arg in args:
            if not isinstance(arg, (int, float)):

                # ================= RAISE TYPE ERROR =================
                raise TypeError(f"All coefficients must be int or float, got {type(arg).__name__}")



    # ==================== SUBCLASS INIT CHECK =================

    # Advanced: this special method is called automatically
    # whenever a subclass of this class is created.
    # It allows customization or tracking of subclass behavior.
    # 'cls' refers to the new subclass being defined.

    def __init_subclass__(cls):


        # ================= CHECK FOR DEGREE ATTRIBUTE =================

        # hasattr returns a boolean indicating if the class has the specified attribute
        # we are looking for the 'degree' attribute
        if not hasattr(cls, 'degree'):


            # ================= RAISE ATTRIBUTE ERROR =================

            # AttributeError warns the developer that they forgot to define 'degree'
            raise AttributeError(f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'")


    # ==================== ABSTRACT METHODS =================

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


    # =================== IMPLEMENT ABSTRACT METHODS =================

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

lin_eq = LinearEquation(2,3) # Pass the correct number of args when instantiating (e.g., LinearEquation(2, 3))
                                   # or you will get a TypeError because of line 40 where we check args length
                                   # and line 42 where we raise the TypeError

# eq = Equation()  # commented out: abstract classes cannot be instantiated directly