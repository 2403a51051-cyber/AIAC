"""
A simple calculator implemented with a class that uses __init__ to set operands.

Exposed functionality:
- Calculator: holds two operands and provides arithmetic operations
- calculate: method to evaluate an operator string

When executed as a script, provides a minimal CLI:
    python Task0.py <operator> <left> <right>

Supported operators: +, -, *, /, %, **
"""

from __future__ import annotations

import sys
from typing import Union


Number = Union[int, float]


class Calculator:
    """Calculator that stores two operands and performs operations.

    The operands are provided at construction time via __init__.
    """

    def __init__(self, left_operand: Number, right_operand: Number) -> None:
        """Initialize the calculator with two operands.

        Args:
            left_operand: The left-hand numeric operand.
            right_operand: The right-hand numeric operand.
        """
        self.left_operand: Number = left_operand
        self.right_operand: Number = right_operand

    def add(self) -> Number:
        return self.left_operand + self.right_operand

    def subtract(self) -> Number:
        return self.left_operand - self.right_operand

    def multiply(self) -> Number:
        return self.left_operand * self.right_operand

    def divide(self) -> Number:
        if self.right_operand == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.left_operand / self.right_operand

    def modulo(self) -> Number:
        if self.right_operand == 0:
            raise ZeroDivisionError("Cannot modulo by zero")
        return self.left_operand % self.right_operand

    def power(self) -> Number:
        return self.left_operand ** self.right_operand

    def calculate(self, operator: str) -> Number:
        """Dispatch calculation based on the operator string.

        Supported operators:
            +, -, *, /, %, **
            Also accepts words: add, sub, mul, div, mod, pow
        """
        mapping = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
            "%": self.modulo,
            "**": self.power,
            # word aliases
            "add": self.add,
            "sub": self.subtract,
            "subtract": self.subtract,
            "mul": self.multiply,
            "multiply": self.multiply,
            "div": self.divide,
            "divide": self.divide,
            "mod": self.modulo,
            "modulo": self.modulo,
            "pow": self.power,
            "power": self.power,
        }

        if operator not in mapping:
            raise ValueError(f"Unsupported operator: {operator}")
        return mapping[operator]()


def _parse_number(raw: str) -> Number:
    """Parse a string into int or float as appropriate."""
    try:
        if "." in raw or "e" in raw.lower():
            return float(raw)
        return int(raw)
    except ValueError:
        # Fallback to float to allow inputs like ".5"
        return float(raw)


def _cli(argv: list[str]) -> int:
    if len(argv) != 4:
        print("Usage: python Task0.py <operator> <left> <right>")
        print("Operators: +, -, *, /, %, ** (or add, sub, mul, div, mod, pow)")
        return 2
    operator = argv[1]
    left = _parse_number(argv[2])
    right = _parse_number(argv[3])
    calc = Calculator(left, right)
    try:
        result = calc.calculate(operator)
    except Exception as exc:  # Keep CLI simple
        print(f"Error: {exc}")
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli(sys.argv))



