from bson.objectid import ObjectId
from src.models.repositories.orders_repository import OrdersRepository


class CollectionMock:
    """Simula o comportamento de uma coleção do PyMongo"""

    def __init__(self) -> None:
        self.insert_one_called_with = None
        self.find_called_with = None
        self.find_returned_value = []

    def insert_one(self, document: dict) -> None:
        self.insert_one_called_with = document

    def find(self, doc_find: dict) -> list:
        self.find_called_with = doc_find
        return self.find_returned_value


class DbCollectionMock:
    """Simula o gerenciador de conexões que entrega coleções"""

    def __init__(self) -> None:
        self.get_collection_called_with = None
        self.get_collection_mock = CollectionMock()

    def get_collection(self, collection_name: str) -> CollectionMock:
        self.get_collection_called_with = collection_name
        return self.get_collection_mock


def test_insert_document_with_custom_mocks():
    db_mock = DbCollectionMock()
    orders_repository = OrdersRepository(db_mock)

    document_to_insert = {"cliente": "Luis Litt", "cupom": True}

    orders_repository.insert_document(document_to_insert)

    assert db_mock.get_collection_called_with == "orders"
    assert db_mock.get_collection_mock.insert_one_called_with == document_to_insert


def test_select_many_with_custom_mocks():
    db_mock = DbCollectionMock()
    simulated_data = [
        {
            "_id": ObjectId("6a0510f70fd15fa1470e1bce"),
            "cliente": "Luis Litt",
            "cupom": True,
        },
        {
            "_id": ObjectId("6a11bb427fdb0af931eea8d3"),
            "cliente": "Lia Evellyn",
            "cupom": True,
        },
    ]

    db_mock.get_collection_mock.find_returned_value = simulated_data

    orders_repository = OrdersRepository(db_mock)
    seach_filter = {"cupom": True}

    reponse = orders_repository.select_many(seach_filter)

    assert db_mock.get_collection_called_with == "orders"
    assert db_mock.get_collection_mock.find_called_with == seach_filter
    assert reponse == simulated_data
    assert len(reponse) == 2
    assert reponse[0]["cliente"] == "Luis Litt"
