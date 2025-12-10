import math

class Calculator:
    # --- Basic operations ---
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    # --- Advanced operations ---
    def log(self, a, base=10):
        if a <= 0:
            raise ValueError("Log domain error")
        return math.log(a, base)

    def square(self, a): return a * a
    def sin(self, a): return math.sin(math.radians(a))
    def cos(self, a): return math.cos(math.radians(a))
    def sqrt(self, a):
        if a < 0:
            raise ValueError("Square root domain error")
        return math.sqrt(a)
    def percent(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero for percentage")
        return (a / b) * 100
