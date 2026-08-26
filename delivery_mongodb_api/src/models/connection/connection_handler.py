import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError

load_dotenv()


class DBConnectionHandler:
    def __init__(
        self,
        connection_string: str | None = None,
        database_name: str | None = None,
    ) -> None:
        self.__connection_string = (
            connection_string
            or os.getenv("MONGO_URI")
            or "mongodb://localhost:27017/"
        )
        self.__database_name = (
            database_name or os.getenv("MONGO_DATABASE") or "rocket_db"
        )
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self) -> None:
        if self.__client is None:
            client = MongoClient(
                self.__connection_string,
                serverSelectionTimeoutMS=5000,
            )
            try:
                client.admin.command("ping")
            except PyMongoError as error:
                client.close()
                raise ConnectionError(
                    "Nao foi possivel conectar ao MongoDB. "
                    "Verifique se o servidor esta ativo e se MONGO_URI esta correta."
                ) from error

            self.__client = client
            self.__db_connection = client[self.__database_name]

    def get_db_connection(self):
        if self.__db_connection is None:
            raise RuntimeError("Conecte ao MongoDB antes de solicitar o banco de dados.")
        return self.__db_connection

    def close_connection(self) -> None:
        if self.__client is not None:
            self.__client.close()
            self.__client = None
            self.__db_connection = None


db_connection_handler = DBConnectionHandler()
