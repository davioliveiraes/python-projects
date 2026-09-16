import pytest
from .registry_updater_validator import registry_update_validator

def test_registry_update_validator():
    body = {
        "data": {
            "name": "Harvey Specter",
            "address": "Bay-Adelaide Centre, em Nova York",
            "cupom": True
        }
    }

    registry_update_validator(body)

def test_registry_update_validator_partial():
    body = {
        "data": {
            "address": "Person Specter Litt, 601 Lexington Avenue"
        }
    }
    registry_update_validator(body)

def test_registry_update_validator_with_errors():
    body_with_error = {
        "data": {
            "name": "Harvey Specter",
            "address": "Bay-Adelaide Centre, em Nova York",
            "cupom": "True"
        }
    }

    with pytest.raises(Exception):
        registry_update_validator(body_with_error)

def test_registry_update_validator_with_unknown_field():
    body_with_error = {
        "data": {
            "name": "Harvey Specter",
            "items": [
                {"item": "Café", "quantidade": 1}
            ]
        }
    }

    with pytest.raises(Exception):
        registry_update_validator(body_with_error)
