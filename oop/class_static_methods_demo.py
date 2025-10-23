# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method that doesn't need class/instance data"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method that can access class attributes"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b