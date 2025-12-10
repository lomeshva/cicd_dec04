import pytest
from src.calculator import Calculator

calc = Calculator()

# --- Basic tests ---
def test_add(): assert calc.add(5, 3) == 8
def test_subtract(): assert calc.subtract(10, 4) == 6
def test_multiply(): assert calc.multiply(6, 7) == 42
def test_divide(): assert calc.divide(8, 2) == 4
def test_divide_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)

# --- Advanced tests ---
def test_log(): assert round(calc.log(100, 10)) == 2
def test_log_invalid():
    with pytest.raises(ValueError):
        calc.log(0)

def test_square(): assert calc.square(5) == 25
def test_sin(): assert round(calc.sin(90), 5) == 1
def test_cos(): assert round(calc.cos(0), 5) == 1
def test_sqrt(): assert calc.sqrt(9) == 3
def test_sqrt_negative():
    with pytest.raises(ValueError):
        calc.sqrt(-4)
def test_percent(): assert calc.percent(50, 200) == 25
def test_percent_zero():
    with pytest.raises(ValueError):
        calc.percent(10, 0)
