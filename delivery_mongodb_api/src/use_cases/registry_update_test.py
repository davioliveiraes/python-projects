from src.main.http_types.http_request import HttpRequest
from .registry_update import RegistryUpdate

class UpdaterRepositoryMock:
    def __init__(self) -> None:
        self.edit_registry_att = {}

    def edit_registry(self, order_id: str, update_fields: dict) -> None:
        self.edit_registry_att["order_id"] = order_id
        self.edit_registry_att["update_fields"] = update_fields

class UpdaterRepositoryMockError:
    def edit_registry(self, order_id: str, update_fields: dict) -> None:
        raise Exception("Erro aqui")

def test_update():
    repo = UpdaterRepositoryMock()
    registry_update = RegistryUpdate(repo) # type: ignore

    mock_update = HttpRequest(
        path_params = { "order_id": "1234567890" },
        body = {
            "data": {
                "name": "Naruto Uzumaki",
                "address": "rua de Konoha, 7",
                "cupom": True
            }
        }
    )

    response = registry_update.update(mock_update)

    assert repo.edit_registry_att["order_id"] == "1234567890"
    assert "name" in repo.edit_registry_att["update_fields"]
    assert "address" in repo.edit_registry_att["update_fields"]
    assert "cupom" in repo.edit_registry_att["update_fields"]

    assert response.status_code == 200
    assert response.body["data"]["order_id"] == "1234567890"
    assert response.body["data"]["count"] == 1
    assert response.body["data"]["type"] == "Order"

def test_update_error():
    repo = UpdaterRepositoryMockError()
    registry_update = RegistryUpdate(repo) # type: ignore

    mock_update = HttpRequest(
        path_params = { "order_id": "1234567890" },
        body = { "data": { "name": 123 } }
    )

    response = registry_update.update(mock_update)

    assert response.status_code == 422
    assert "errors" in response.body
