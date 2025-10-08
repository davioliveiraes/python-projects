from typing import Dict, List
from flask import request as FlaskRequest 
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
   '''
   Neste desafio, você vai implementar uma nova rota chamada "calculator_4" seguindo o exemplo dado pelo instrutor no módulo. A rota deve calcular a média entre uma lista de números fornecida em uma requisição POST, aplicando todas as boas práticas ensinadas.
   '''

   def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
      body = request.json
      input_data = self.__validate_body(body)
      calculated_number = self.__process_data(input_data)
      formated_response = self.__format_response(calculated_number)

      return formated_response
   
   def __validate_body(self, body: Dict) -> List[float]:
      if "numbers" not in body:
         raise HttpUnprocessableEntityError("Body mal formatado")
      
      input_data = body["numbers"]
      return input_data

   def __process_data(self, input_data: List[float]) -> float:
      sum_numbers = 0
      for num in input_data:
         sum_numbers += num
      average_numbers = sum_numbers / len(input_data)

      return average_numbers

   def __format_response(self, calculated_number: float) -> Dict:
      return {
         "data": {
            "Calculator": 4,
            "result": round(calculated_number, 2)
         }
      }


   
   

