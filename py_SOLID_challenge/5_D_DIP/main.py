from abc import ABC, abstractmethod
from typing import Dict, Optional, List
from datetime import datetime, timedelta
import json

# Abstrações (Interfaces) - O contrato que todos devem seguir

class UserRepositoryInterface(ABC):
    """Interface - Repositório de Usuários"""

    @abstractmethod
    def save(self,  user_data: dict) -> dict:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[dict]:
        pass

    @abstractmethod
    def update(self, email: str, user_data: dict) -> dict:
        pass

class PasswordHasherInterface(ABC):
    """Interface - Hasher de senhas"""

    @abstractmethod
    def hash(self, password: str) -> str:
        pass

    @abstractmethod
    def verify(self, password: str, hashed: str) -> bool:
        pass

class TokenServiceInterface(ABC):
    """Interface - Seriço de tokens de sessão"""

    @abstractmethod
    def generate_token(self, user_data: dict) -> str:
        pass

    @abstractmethod
    def validate_token(self, token: str) -> Optional[str]:
        pass

    @abstractmethod
    def revoke_token(self, token: str) -> bool:
        pass

class AuthLoggerInterface(ABC):
    """Interface - Logger de autenticação"""

    @abstractmethod
    def log_success(self, email: str, action: str) -> None:
        pass

    @abstractmethod
    def log_failure(self, email: str, action: str, reason: str) -> None:
        pass

# Implementações de Baixo Nível

class PostgresUserRepository(UserRepositoryInterface):
    """Repositórios de Usuário - Usando o Postgresql"""

    def __init__(self):
        self.database: Dict[str, dict] = {}
    
    def save(self, user_data: dict) -> dict:
        email = user_data["email"]
        self.database[email] = {
            **user_data,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "storage": "PostgreSQL"
        }
        print(f"   [PostgreSQL] Usuário '{email}' salvo com sucesso")
        return self.database[email]
    
    def find_by_email(self, email: str) -> Optional[dict]:
        user = self.database.get(email)
        if user:
            print(f"   [PostgreSQL] Usuário '{email}' encontrado")
        else:
            print(f"   [PostgreSQL] Usuário '{email}' não encontrado")
        return user

    def update(self, email: str, user_data: dict) -> dict:
        if email in self.database:
            self.database[email].update(user_data)
            print(f"   [PostgreSQL] Dados do usuário '{email}' atualizados")
        return self.database.get(email, {})

class MongoUserRepository(UserRepositoryInterface):
    """Repositórios de Usuário - Usando o MongoDB"""

    def __init__(self):
            self.collection: Dict[str, dict] = {}
        
    def save(self, user_data: dict) -> dict:
            email = user_data["email"]
            self.collection[email] = {
                **user_data,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "storage": "MongoDB"
            }
            print(f"  [MongoDB] Documento do usuário '{email}' inserido na collecton")
            return self.collection[email]
    
    def find_by_email(self, email: str) -> Optional[dict]:
        user = self.collection.get(email)
        if user:
            print(f"  [MongoDB] Documento do usuário '{email}' encontrado")
        else:
            print(f"  [MongoDB] Documento do usuário '{email}' não encontrado")
        return user

    def update(self, email: str, user_data: dict) -> dict:
        if email in self.collection:
            self.collection[email].update(user_data)
            print(f"  [MongoDB] Documento do usuário '{email}' atualizado")
        return self.collection.get(email, {})

class BCryptPasswordHasher(PasswordHasherInterface):
    """Hasher de senhas usadas BCrypt"""

    def hash(self, password: str) -> str:
        hashed = f"$2b$12${password[::-1]}...bcrypt_hash"
        print(f"  [BCrypt] senha hesheada com salt rounds=12")
        return hashed
    
    def verify(self, password: str, hashed: str) -> bool:
        expected = f"$2b$12${password[::-1]}...bcrypt_hash"
        is_valid = expected == hashed
        print(f"  [Bcrypt] Verificação de senha {'válida' if is_valid else 'inválida'}")
        return is_valid

class Argon2PasswordHasher(PasswordHasherInterface):
    """Hasher de senhas Usando Argon2"""

    def hash(self, password: str) -> str:
        hashed = f"$argon2id$v=19${password[::-1]}...argon2_hash"
        print("  [Argon2] Senha hasheada com Argon2id v19")
        return hashed
    
    def verify(self, password: str, hashed: str) -> bool:
        expected = f"$argon2id$v=19${password[::-1]}...argon2_hash"
        is_valid = expected == hashed
        print(f"  [Argon2] Verificação de senha {'válida' if is_valid else 'inválida'}")
        return is_valid

class JWTTokenService(TokenServiceInterface):
    """Serviço de tokens usando JWT"""

    def __init__(self):
        self.active_tokens: Dict[str, dict] = {}
    
    def generate_token(self, user_data: Dict) -> str:
        token = f"dAKjdansalsancassow.{user_data['email']}.jwt_signature"
        self.active_tokens[token] = {
            "user": user_data['email'],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "expires_at": (datetime.now() + timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"  [JWT] Token gerado com expiração de 24h")
        return token
    
    def validate_token(self, token: str) -> str | None:
        token_data = self.active_tokens.get(token)
        if token_data:
            print(f"  [JWT] Token válido para o usuário '{token_data['user']}'")
            return token_data # type: ignore
        print(f"  [JWT] Token inválido ou expierado")
        return None
    
    def revoke_token(self, token: str) -> bool:
        if token in self.active_tokens:
            del self.active_tokens[token]
            print("  [JWT] Token revogado com sucesso")
            return True
        print(f"   [JWT] Token não encontrado para revogação")
        return False

class OpaqueTokenService(TokenServiceInterface):
    """Serviço de tokens opacos armazenados no Redis"""

    def __init__(self):
        self.token_store: Dict[str, dict] = {}
        self.token_counter = 0
    
    def generate_token(self, user_data: Dict) -> str:
        self.token_counter += 1
        token = f"opk_{self.token_counter}_{''.join(reversed(user_data['email']))}"
        self.token_store[token] = {
            "user": user_data["email"],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "expires_at": (datetime.now() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"  [Redis/Opaque] Token opaco gerado e armazenado no Redis (TTL: 8h)")
        return token
    
    def validate_token(self, token: str) -> Optional[dict]:
        token_data = self.token_store.get(token)
        if token_data:
            print(f"  [Redis/Opaque] Token válido - sessão ativa para '{token_data['user']}'")
            return token_data
        print(f"  [Redis/Opaque] Token não encontrado no Redis")
        return None

    def revoke_token(self, token: str) -> bool:
        if token in self.token_store:
            del self.token_store[token]
            print(f"   [Redis/Opaque] Token removido do Redis")
            return True
        print(f"   [Redis/Opaque] Token não encontrado no Redis")
        return False

class ConsoleAuthLogger(AuthLoggerInterface):
    """Logger de autenticação via console"""

    def log_success(self, email: str, action: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f" [LOG] {timestamp} | SUCESSO | {action} | {email}")

    def log_failure(self, email: str, action: str, reason: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"  [LOG] {timestamp} | FALHA | {action} | {email} | Motivo: {reason}")

class FileAuthLogger(AuthLoggerInterface):
    """Logger de autenticação via arquivo"""

    def __init__(self):
        self.logs: List[str] = []

    def log_success(self, email: str, action: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} | SUCESSO | {action} | {email}"
        self.logs.append(log_entry)
        print(f"  [FILE LOG] Registro gravado: {log_entry}")

    def log_failure(self, email: str, action: str, reason: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} | FALHA | {action} | {email} | {reason}"
        self.logs.append(log_entry)
        print(f"  [FILE LOG] Registro gravado: {log_entry}")
    
    def get_logs(self) -> List[str]:
        return self.logs.copy()

# Implementação de Alto Nível - Depende apenas de abstrações

class AuthenticationService:
    """Serviço de autenticação de alto nível. Depende de apenas de abstrações (interfaces), nunca de implementações concretas. Isso é O Princípio da Inversão de Dependência (DIP)"""

    def __init__(self, 
                 user_repository: UserRepositoryInterface,
                 password_hasher: PasswordHasherInterface,
                 token_service: TokenServiceInterface,
                 auth_logger: AuthLoggerInterface):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.token_service = token_service
        self.auth_logger = auth_logger
    
    def register(self, name: str, email: str, password: str) -> dict:
        existing = self.user_repository.find_by_email(email)
        if existing:
            self.auth_logger.log_failure(email, "REGISTRO", "E-mail já cadastrado")
            return {"status": "erro", "mensagem": "E-mail já cadastrado"}
    
        hashed_password = self.password_hasher.hash(password)

        user_data = {
            "name": name,
            "email": email,
            "password": hashed_password,
            "active": True
        }

        saved_user = self.user_repository.save(user_data)
        self.auth_logger.log_success(email, "REGISTRO")

        return {
            "status": "sucesso",
            "mensagem": "Usuário registrado com sucesso",
            "usuario": saved_user["name"]
        }

    def login(self, email: str, password: str) -> dict:
        user = self.user_repository.find_by_email(email)
        if not user:
            self.auth_logger.log_failure(email, "LOGIN", "Usuário não encontrado")
            return {"status": "erro", "mensagem": "Credenciais inválidas"}
        
        if not self.password_hasher.verify(password, user["password"]):
            self.auth_logger.log_failure(email, "LOGIN", "Senha incorreta")
            return {"status": "erro", "mensagem": "Credenciais inválidas"}
        
        token = self.token_service.generate_token(user)
        self.user_repository.update(
            email, {"last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )
        self.auth_logger.log_success(email, "LOGIN")

        return {
            "status": "sucesso",
            "mensagem": "Login realizado com sucesso",
            "token": token,
            "usuario": user["name"]
        }
    
    def validate_session(self, token: str) -> dict:
        token_data = self.token_service.validate_token(token)
        if token_data:
            return {
                "status": "sucesso",
                "sessao_ativa": True,
                "usuario": token_data["user"] # type: ignore
            }
        return {
            "status": "erro",
            "sessao_ativa": False,
            "mensagem": "Sessão expirada ou inválida"
        }
    
    def logout(self, token: str) -> dict:
        token_data = self.token_service.validate_token(token)
        if token_data:
            self.token_service.revoke_token(token)
            self.auth_logger.log_success(token_data["user"], "LOGOUT") # type: ignore
            return {"status": "sucesso", "mensagem": "Logout realizado com sucesso"}
        return {"status": "erro", "mensagem": "Token inválido"}

# Demonstração

def main():
    print("=" * 70)
    print(" DEMONSTRAÇÃO DO PRINCÍPIO D - INVERSÃO DE DEPENDÊNCIA (DIP) ")
    print(" Sistema de Autenticação de Usuários ")
    print("=" * 70)

    # Cenário 1
    print("\n" + "-" * 70)
    print(" CENÁRIO 1: PostgreSQL + BCrypt + JWT + Console Logger ")
    print("-" * 70)

    auth_service_1 = AuthenticationService(
        user_repository=PostgresUserRepository(),
        password_hasher=BCryptPasswordHasher(),
        token_service=JWTTokenService(),
        auth_logger=ConsoleAuthLogger()
    )

    print("\n >> Registrando usuário...")
    result = auth_service_1.register("Naruto Usumaki", "naruto@email.com", "senha_segura_123")
    print(f"  Resultado: {json.dumps(result, ensure_ascii=False, indent=2)}")

    print("\n Realizando login...")
    result = auth_service_1.login("naruto@email.com", "senha_segura_123")
    print(f"  Resultado: {json.dumps(result, ensure_ascii=False, indent=2)}")
    token_1 = result.get("token", "")

    print("\n>> Validando sessão...")
    result = auth_service_1.validate_session(token_1)
    print(f"  Resultado: {json.dumps(result, ensure_ascii=False, indent=2)}")

    print("\n Realizando logout...")
    result = auth_service_1.logout(token_1)
    print(f"  Resultado: {json.dumps(result, ensure_ascii=False, indent=2)}")

    print("\n Validando sessõa após logout...")
    result = auth_service_1.validate_session(token_1)
    print(f"  Resultado: {json.dumps(result, ensure_ascii=False, indent=2)}")

    # Cenário 2
    print("\n" + "-" * 70)
    print(" CENÁRIO 2: MongoDB + Argon2 + Opaque Token (Redis) + File Logger")
    print("-" * 70)

    file_logger = FileAuthLogger()
    auth_service_2 = AuthenticationService(
        user_repository=MongoUserRepository(),
        password_hasher=Argon2PasswordHasher(),
        token_service=OpaqueTokenService(),
        auth_logger=file_logger
    )

    print("\n>> Registrando usuário...")
    result = auth_service_2.register("Sasuke Uchiha", "sasuke@email.com", "senha_segura_123_2")
    print(f"  Resultado: {json.dumps(result, ensure_ascii=False, indent=2)}")

    print("\n>> Realizando login...")
    result = auth_service_2.login("sasuke@email.com", "senha_segura_123_2")
    print(f"  Resultado: {json.dumps(result, ensure_ascii=False, indent=2)}")
    token_2 = result.get("token", "")

    print("\n>> Tentando login com a senha errada...")
    result = auth_service_2.login("sasuke@email.com", "senha_segura")
    print(f"  Resultado: {json.dumps(result, ensure_ascii=False, indent=2)}")

    print("\n>> Tentando registrar e-mail duplicado...")
    result = auth_service_2.register("Sasuke clone", "gaara@email.com", "senha_segura")
    print(f"  Resultado: {json.dumps(result, ensure_ascii=False, indent=2)}")

    print("\n>> Validando sessão ativa...")
    result = auth_service_2.validate_session(token_2)
    print(f"  Resultado: {json.dumps(result, ensure_ascii=False, indent=2)}")

    # Logs de FileLogger
    print("\n" + "-" * 70)
    print(" LOGS REGISTRADOS (FileAuthLogger) ")
    print("-" * 70)
    for log in file_logger.get_logs():
        print(f"  {log}")

    # Resumo do DIP
    print("\n" + "=" * 70)
    print(" PRINCÍPIO DA INVERSÃO DE DEPENDÊNCIA (DIP) ")
    print("=" * 70)
    print("""

        O  AuthenticationService (Módulo de ALTO NÍVEL) NÃO depende:
        - PostgresUserRepository ou MongoUserRepository
        - BCryptPasswordHasher ou Argon2PasswordHasher
        - JWTTokenService ou OpaqueTokenService
        - ConsoleAuthLogger ou FileAuthLogger

        Ele depende APENAS das ABSTRAÇÕES (interfaces)
        - UserRepositoryInterface
        - PasswordHashedInterface
        - TokenServiceInterface
        - AuthLoggerInterface

        Isso permite trocar QUALQUER implementação sem alterar o código do serviço de autenticação. As dependências são INJETADAS via construtor, seguindo o princípio:
        
        "Dependa de abstrações, não de implementações concretas."

    """)
    print("=" * 70)

if __name__ == "__main__":
    main()
