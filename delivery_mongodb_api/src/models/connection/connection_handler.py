from pymongo import MongoClient


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "mongodb://{}:{}@{}:{}/?authSource=admin".format(
            "admin",
            "password",
            "localhost",
            "27017",
        )
        self.__databse_name = "rocket_db"
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self) -> None:
        if self.__client is None:
            self.__client = MongoClient(self.__connection_string)
            self.__db_connection = self.__client[self.__databse_name]

    def get_db_connection(self):
        return self.__db_connection
