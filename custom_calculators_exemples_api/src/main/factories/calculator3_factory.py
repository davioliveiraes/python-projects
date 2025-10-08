from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumPyHandler

def calculator3_factory():
   numpy_handler = NumPyHandler()
   calc = Calculator3(numpy_handler)
   return calc
