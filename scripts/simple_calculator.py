class SimpleCalculator:
    def sum(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "ERROR"
