import pytest
from pprint import pprint
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

@pytest.fixture
def conn():
    db_connection_handler = DBConnectionHandler()
    db_connection_handler.connect_to_db()
    yield db_connection_handler.get_db_connection()
    db_connection_handler.close_connection()


@pytest.mark.skip(reason="interacao com banco")
def test_insert_document(conn):
    orders_repository = OrdersRepository(conn)
    my_doc = {"ola": "Mundo"}
    orders_repository.insert_document(my_doc)


@pytest.mark.skip(reason="interacao com banco")
def test_list_insert_documents(conn):
    orders_repository = OrdersRepository(conn)
    list_of_documents = [{"exe1": "aqui1"}, {"exe2": "aqui2"}, {"exe3": "aqui3"}]
    orders_repository.insert_list_of_documents(list_of_documents)

@pytest.mark.skip(reason="interacao com banco")
def test_select_many(conn):
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom": True }
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)
    for i in response:
        pprint(i)
        print("-" * 40)

@pytest.mark.skip(reason="interacao com banco")
def test_select_one(conn):
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom": True }
    response = orders_repository.select_one(doc_filter)
    print()
    pprint(response)

@pytest.mark.skip(reason="interacao com banco")
def test_select_with_properties(conn):
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_many_with_properties({"cupom": True}, {"_id": 0, "cupom": 0})
    print()
    print(response)
    for doc in response:
        pprint(doc)
        print("-" * 40)

@pytest.mark.skip(reason="interacao com banco")
def test_select_if_property_exists(conn):
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists("address", {"id": 0, "itens": 0})
    print()
    print(response)
    for doc in response:
        pprint(doc)
        print("-" * 40)

@pytest.mark.skip(reason="interacao com banco")
def test_select_many_with_multiple_filter(conn):
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "cupom": True,
        "itens.refrigerante": { "$exists": True },
    } # Semelhante a uma busca AND em SQL

    response = orders_repository.select_many(doc_filter)
    print()
    print(response)
    for doc in response:
        pprint(doc)
        print("-" * 40)

@pytest.mark.skip(reason="interacao com banco")
def test_select_many_with_or_filter(conn):
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or": [
            {"address": { "$exists": True} },
            {"itens.doce.tipo": "chocolate"}
        ]
    } # Semelhante a uma busca OR em SQL

    response = orders_repository.select_many(doc_filter)
    print()
    print(response)
    for doc in response:
        pprint(doc)
        print("-" * 40)

@pytest.mark.skip(reason="interacao com banco")
def test_select_by_object_id(conn):
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_by_object_id("6a0510f70fd15fa1470e1bce")
    print()
    pprint(response)
    print("-" * 40)

@pytest.mark.skip(reason="interacao com banco")
def test_edit_registry(conn):
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_registry()

@pytest.mark.skip(reason="interacao com banco")
def test_edit_many_registries(conn):
    order_repository = OrdersRepository(conn)
    order_repository.edit_many_registries()

@pytest.mark.skip(reason="interacao com banco")
def test_edit_registry_with_increment(conn):
    order_repository = OrdersRepository(conn)
    order_repository.edit_registry_with_increment()

@pytest.mark.skip(reason="interacao com banco")
def test_delete_registry(conn):
    order_repository = OrdersRepository(conn)
    order_repository.delete_registry()

@pytest.mark.skip(reason="interacao com banco")
def test_delete_many_registries(conn):
    order_repository = OrdersRepository(conn)
    order_repository.delete_many_registries()
