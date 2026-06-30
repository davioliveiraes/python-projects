from src.main.http_types.http_request import HttpRequest
from .registry_order import RegistryOrder

class OrdersRepositoryMock:
    def __init__(self) -> None:
        self.insert_document_att = {}

    def insert_document(self, document: dict) -> None:
        self.insert_document_att["document"] = document

class OrdersRepositoryMockError:
    def insert_document(self, document: dict) -> None:
        raise Exception("Erro aqui")

def test_registry():
    repo = OrdersRepositoryMock()
    registry_order = RegistryOrder(repo) # type: ignore

    mock_registry = HttpRequest(
        body = {
            "data": {
                "name": "Naruto",
                "address": "rua de Konoha",
                "cupom": False,
                "items": [
                    { "item": "Refrigerante", "quantidade": 2 },
                    { "item":  "pizza", "quantidade": 3 }
                ]
            }
        }
    )

    response = registry_order.registry(mock_registry)

    assert "name" in repo.insert_document_att["document"]
    assert "address" in repo.insert_document_att["document"]
    assert "created_at" in repo.insert_document_att["document"]

    assert response.status_code == 201
    assert response.body["data"]["count"] == 1
    assert response.body["data"]["type"] == "Order"
