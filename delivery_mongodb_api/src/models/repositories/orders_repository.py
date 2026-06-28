from bson.objectid import ObjectId
from src.models.repositories.interfaces.orders_repository import OrdersRepositoryInterface


class OrdersRepository(OrdersRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_find: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_find)
        return data

    def select_one(self, doc_find: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(doc_find)
        return response

    def select_many_with_properties(self, doc_find: dict, properties: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_find, properties)
        return data

    def select_if_property_exists(self, property_name: str, properties: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find({property_name: { "$exists": True }}, properties)
        return response

    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({"_id": ObjectId(object_id)})
        return data

    def edit_registry(self) -> None:
        colection = self.__db_connection.get_collection(self.__collection_name)
        colection.update_one(
            {"_id": ObjectId("6a11bb427fdb0af931eea8d3")},  # Filtros
            {"$set": {"itens.refrigerante.tipo": "pepsi"}},  # Edição
        )

    def edit_many_registries(self) -> None:
        colection = self.__db_connection.get_collection(self.__collection_name)
        colection.update_many(
            {"itens.refrigerante": {"$exists": True}}, # Filtros
            {"$set": {"itens.refrigerante.quantidade": 5} }, # Edição
        )

    def edit_registry_with_increment(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId("6a11bb427fdb0af931eea8d3") }, # Filtros
            { "$inc": {"itens.pizza.quantidade": 10} }, # Edição
        )

    def delete_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({"_id": ObjectId("6a0510f70fd15fa1470e1bce")})

    def delete_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many({"itens.refrigerante": {"$exists": True}})
