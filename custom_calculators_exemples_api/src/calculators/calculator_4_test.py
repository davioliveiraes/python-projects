from typing import Dict
from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
   def __init__(self, body: Dict) -> None:
      self.json = body
   
def test_calculate_integration():
   mock_request = MockRequest({ "numbers": [9.1, 8.5, 6.7, 7.8] })
   calculator_4 = Calculator4()
   formated_response = calculator_4.calculate(mock_request)

   assert isinstance(formated_response, dict)
   assert formated_response == {'data': {'Calculator': 4, 'result': 8.03}}

def test_calculate_with_body_error():
   mock_request = MockRequest({ "values": [1, 2, 3, 4] })
   calculator_4 = Calculator4()
   
   with raises(Exception) as excinfo:
      calculator_4.calculate(mock_request)
   
   assert str(excinfo.value) == "Body mal formatado"

