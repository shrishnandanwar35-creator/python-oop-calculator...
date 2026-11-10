# Python OOP Calculator

A command-line calculator built with object-oriented programming in Python.

## Features

- Addition, subtraction, multiplication, division, powers, and modulus
- Validation for division or modulus by zero
- Calculation history stored inside the `Calculator` object
- Menu-based command-line interface
- Unit tests using Python's built-in `unittest` module

## OOP concepts used

- **Class and objects:** `Calculator` is the blueprint; `calculator` in `main.py` is an object.
- **Encapsulation:** history is stored in the private `_history` attribute and exposed safely through `get_history()`.
- **Abstraction:** each arithmetic operation is a public method such as `add()` or `divide()`.
- **Custom exceptions:** `CalculatorError` communicates calculation-specific problems clearly.
- **Data class:** each `Calculation` object stores one history entry.

## Run the program

```bash
python main.py
```

## Run the tests

From the project folder, run:

```bash
python -m unittest discover -s tests -t . -v
```

## Publish to GitHub

1. Create an empty GitHub repository called `python-oop-calculator` (do not add a README, license, or `.gitignore` on GitHub).
2. In this project folder, run:

```bash
git init
git add .
git commit -m "Create OOP Python calculator"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/python-oop-calculator.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.
