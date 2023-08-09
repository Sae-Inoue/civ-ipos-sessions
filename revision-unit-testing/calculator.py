#class CalculatorError(Exception)

class Calculator:
    def add(self,a,b):
        if not isinstance(a,int) or not isinstance(b,int):
            raise TypeError
        return a + b

    def multiply(self,a,b):
        if not isinstance(a, int) or not isinstance(b,int):
            raise TypeError("Please Enter integer!!")
        return a * b

    def divide(self,a, b):
        return a / b



