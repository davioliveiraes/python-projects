from unittest.mock import MagicMock, patch

import pytest
from pymongo.errors import ServerSelectionTimeoutError

from .connection_handler import DBConnectionHandler


@patch("src.models.connection.connection_handler.MongoClient")
def test_connect_to_db_checks_server_and_selects_database(mongo_client_mock):
    client = MagicMock()
    database = MagicMock()
    mongo_client_mock.return_value = client
    client.__getitem__.return_value = database

    handler = DBConnectionHandler("mongodb://localhost:27017/", "rocket_db")
    handler.connect_to_db()

    mongo_client_mock.assert_called_once_with(
        "mongodb://localhost:27017/",
        serverSelectionTimeoutMS=5000,
    )
    client.admin.command.assert_called_once_with("ping")
    client.__getitem__.assert_called_once_with("rocket_db")
    assert handler.get_db_connection() is database


@patch("src.models.connection.connection_handler.MongoClient")
def test_connect_to_db_reports_unavailable_server(mongo_client_mock):
    client = mongo_client_mock.return_value
    client.admin.command.side_effect = ServerSelectionTimeoutError("offline")
    handler = DBConnectionHandler("mongodb://localhost:27017/", "rocket_db")

    with pytest.raises(ConnectionError, match="Nao foi possivel conectar"):
        handler.connect_to_db()

    client.close.assert_called_once_with()


def test_get_db_connection_requires_an_active_connection():
    handler = DBConnectionHandler("mongodb://localhost:27017/", "rocket_db")

    with pytest.raises(RuntimeError, match="Conecte ao MongoDB"):
        handler.get_db_connection()
