"""An object-oriented calculator module."""

from __future__ import annotations

from dataclasses import dataclass


class CalculatorError(ValueError):
    """Raised when a calculator operation cannot be completed."""


@dataclass(frozen=True)
class Calculation:
    """Stores one completed calculation."""

    operation: str
    first_number: float
    second_number: float
    result: float


class Calculator:
    """Performs arithmetic operations and remembers calculation history."""

    def __init__(self) -> None:
        self._history: list[Calculation] = []

    def add(self, first_number: float, second_number: float) -> float:
        """Return the sum of two numbers."""
        return self._record("add", first_number, second_number, first_number + second_number)

    def subtract(self, first_number: float, second_number: float) -> float:
        """Return the difference between two numbers."""
        return self._record(
            "subtract", first_number, second_number, first_number - second_number
        )

    def multiply(self, first_number: float, second_number: float) -> float:
        """Return the product of two numbers."""
        return self._record(
            "multiply", first_number, second_number, first_number * second_number
        )

    def divide(self, first_number: float, second_number: float) -> float:
        """Return the quotient of two numbers."""
        self._require_nonzero(second_number, "divide")
        return self._record(
            "divide", first_number, second_number, first_number / second_number
        )

    def power(self, first_number: float, second_number: float) -> float:
        """Raise the first number to the power of the second number."""
        return self._record(
            "power", first_number, second_number, first_number**second_number
        )

    def modulus(self, first_number: float, second_number: float) -> float:
        """Return the remainder after division."""
        self._require_nonzero(second_number, "use modulus with")
        return self._record(
            "modulus", first_number, second_number, first_number % second_number
        )

    def get_history(self) -> tuple[Calculation, ...]:
        """Return completed calculations without exposing internal storage."""
        return tuple(self._history)

    def clear_history(self) -> None:
        """Remove all saved calculations."""
        self._history.clear()

    def _record(
        self, operation: str, first_number: float, second_number: float, result: float
    ) -> float:
        self._history.append(
            Calculation(operation, first_number, second_number, result)
        )
        return result

    @staticmethod
    def _require_nonzero(number: float, action: str) -> None:
        if number == 0:
            raise CalculatorError(f"Cannot {action} zero.")
