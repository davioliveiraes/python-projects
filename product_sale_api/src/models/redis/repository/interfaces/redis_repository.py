from abc import ABC, abstractmethod
from typing import Any


class RedisRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, key: str, value: Any) -> None:
        pass

    @abstractmethod
    def get_key(self, key: str) -> str | None:
        pass

    @abstractmethod
    def insert_hash(self, key: str, field: str, value: Any) -> None:
        pass

    @abstractmethod
    def get_hash(self, key: str, field: str) -> str | None:
        pass

    @abstractmethod
    def insert_ex(self, key: str, value: Any, ex: int) -> None:
        pass

    @abstractmethod
    def insert_hash_ex(self, key: str, field: str, value: Any, ex: int) -> None:
        pass
