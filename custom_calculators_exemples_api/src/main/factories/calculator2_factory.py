from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumPyHandler

def calculator2_factory():
   numpy_handler = NumPyHandler()
   calc = Calculator2(numpy_handler) # type: ignore

   return calc