from typing import Any
from cerberus import Validator
from src.main.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError

def registry_order_validator(body: dict[str, Any]) -> None:
    body_validator = Validator(
        {
            "data": {
                "type": "dict",
                "schema": {
                    "name": {"type": "string", "required": True},
                    "address": {"type": "string", "required": True},
                    "cupom": {"type": "boolean", "required": True},
                    "items": {
                        "type": "list",
                        "schema": {
                            "type": "dict",
                            "schema": {
                                "item": {"type": "string", "required": True},
                                "quantidade": {"type": "integer", "required": True}
                            }
                        }
                    }
                }
            }
        }
    )

    response = body_validator.validate(body)

    if not response:
        raise HttpUnprocessableEntityError(body_validator.errors)
