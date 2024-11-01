import string, secrets, hashlib, base64
from pathlib import Path
from cryptography.fernet import Fernet

class FernetHasher:
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase
    BASE_DIR = Path(__file__).resolve().parent.parent
    KEY_DIR = BASE_DIR / 'keys'

    def __init__(self, key):
        if not isinstance(key, bytes):
            key = key.encode()

        self.fernet = Fernet(key)

    @classmethod
    def _get_random_string(cls, length=25):
        string = ''
        for i in range(length):
            string += secrets.choice(cls.RANDOM_STRING_CHARS)
        return string

    @classmethod
    def create_key(cls, archive=False):
        value = cls._get_random_string()
        hasher = hashlib.sha256(value.encode('utf-8')).digest()
        key = base64.b64encode(hasher)
        if archive:
            return key, cls.archive_key(key)
        return key, None

    @classmethod
    def archive_key(cls, key):
        file = 'key.key'
        while Path(cls.KEY_DIR / file).exists():
            file = f'key_{cls._get_random_string(5)}.key'

        with open(cls.KEY_DIR / file, "wb") as arq:
            arq.write(key)

        return cls.KEY_DIR / file

    def encrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()
        return self.fernet.encrypt(value)

    def decrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()
        try:
            return self.fernet.decrypt(value).decode()
        except InvalidToken as e:
            return 'Token inválido'

# CRIANDO UMA NOVA CHAVE
# criando_chave, arquivo_chave = FernetHasher.create_key(archive=True)
# print(f"Chave gerada e arquivada: {criando_chave}")
# print(f"Arquivo de chave salvo em: {arquivo_chave}")

# CRIPTOGRAFANDO A CHAVE DE ACESSO
# fernet_davi = FernetHasher("g7CB2AOsv4RezinGkOlFZADL6HOpbn8PAtmPQ6SxGfk=")
# print(fernet_davi.encrypt("CHAVE DE ACESSO DAVI"))

# DESCRIPTOGRAFANDO A CHAVE DE ACESSO
# fernet_davi = FernetHasher("g7CB2AOsv4RezinGkOlFZADL6HOpbn8PAtmPQ6SxGfk=")
# print(
#     fernet_davi.decrypt(
#         "gAAAAABnJOWovC8wscJV6CmI2Z1cAqh0szQiBXm2iqA51L7hju8TYXak6wvebzTpP421jaHrZRUze-I9UonOd_b9CXUMytWQV23Ih9cd5CefgFNF6h6JhG0="
#     )
# )
