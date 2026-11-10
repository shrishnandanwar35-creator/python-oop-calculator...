"""Command-line interface for the object-oriented calculator."""

from calculator import Calculator, CalculatorError


OPERATIONS = {
    "1": ("Add", "add"),
    "2": ("Subtract", "subtract"),
    "3": ("Multiply", "multiply"),
    "4": ("Divide", "divide"),
    "5": ("Power", "power"),
    "6": ("Modulus", "modulus"),
}


def get_number(prompt: str) -> float:
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def show_history(calculator: Calculator) -> None:
    """Print every calculation saved by the calculator object."""
    history = calculator.get_history()
    if not history:
        print("No calculations yet.")
        return

    print("\nCalculation history")
    for index, calculation in enumerate(history, start=1):
        print(
            f"{index}. {calculation.operation}: "
            f"{calculation.first_number} and {calculation.second_number} = "
            f"{calculation.result}"
        )


def run() -> None:
    """Run the calculator menu."""
    calculator = Calculator()

    while True:
        print("\n--- OOP Python Calculator ---")
        for key, (label, _) in OPERATIONS.items():
            print(f"{key}. {label}")
        print("7. View history")
        print("8. Clear history")
        print("9. Exit")

        choice = input("Choose an option (1-9): ").strip()

        if choice == "9":
            print("Goodbye!")
            break
        if choice == "7":
            show_history(calculator)
            continue
        if choice == "8":
            calculator.clear_history()
            print("History cleared.")
            continue
        if choice not in OPERATIONS:
            print("Please choose a number from 1 to 9.")
            continue

        first_number = get_number("Enter the first number: ")
        second_number = get_number("Enter the second number: ")
        label, method_name = OPERATIONS[choice]

        try:
            result = getattr(calculator, method_name)(first_number, second_number)
            print(f"{label} result: {result}")
        except CalculatorError as error:
            print(error)


if __name__ == "__main__":
    run()
