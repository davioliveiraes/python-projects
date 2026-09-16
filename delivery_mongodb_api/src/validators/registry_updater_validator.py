from typing import Any
from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


def registry_update_validator(body: Any) -> None:
    body_validator = Validator(
        {
            "data": {
                "type": "dict",
                "schema": {
                    "name": {"type": "string"},
                    "address": {"type": "string"},
                    "cupom": {"type": "boolean"},
                },
            }
        }
    )

    response = body_validator.validate(body)

    if not response:
        raise HttpUnprocessableEntityError(body_validator.errors)
