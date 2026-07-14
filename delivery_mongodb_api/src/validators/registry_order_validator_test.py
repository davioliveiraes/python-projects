import pytest
from .registry_order_validator import registry_order_validator

def test_registry_order_validator():
    body = {
        "data": {
            "name": "Harvey Specter",
            "address": "Bay-Adelaide Centre, em Nova York",
            "cupom": False,
            "items": [
                {"item": "Café", "quantidade": 1},
                {"item": "Rosquinha", "quantidade": 2},
            ]
        }
    }
    registry_order_validator(body)

def test_registry_order_validator_with_errors():
    body_with_error = {
        "data": {
            "name": "Harvey Specter",
            "address": "Bay-Adelaide Centre, em Nova York",
            "cupom": "True",
            "items": [
                {"item": "Café", "quantidade": 1},
                {"item": "Rosquinha", "quantidade": 2},
            ],
        }
    }

    with pytest.raises(Exception):
        registry_order_validator(body_with_error)
