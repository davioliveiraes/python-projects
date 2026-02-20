# 🔄 DIP — Dependency Inversion Principle

Sistema de autenticação de usuários construído para demonstrar o **Princípio D do SOLID**: Inversão de Dependência.

---

## Sobre o Projeto

Implementação prática do DIP aplicado a um sistema de autenticação completo. O serviço de alto nível (`AuthenticationService`) depende **apenas de abstrações**, nunca de implementações concretas — permitindo trocar banco de dados, algoritmo de hash, tipo de token e logger sem alterar uma linha do serviço principal.

---

## Benefícios do DIP

- **Flexibilidade** — troque qualquer implementação sem afetar o núcleo da aplicação
- **Testabilidade** — injete mocks nas interfaces durante os testes
- **Baixo acoplamento** — módulos de alto nível isolados das dependências concretas
- **Extensibilidade** — novas implementações sem modificar código existente (Open/Closed)

---

## Funcionalidades

- Registro de usuário com validação de e-mail duplicado
- Login com verificação de senha hasheada
- Geração e validação de tokens de sessão
- Logout com revogação de token
- Logging de eventos de sucesso e falha

---

## Tecnologias

| Camada | Opção A | Opção B |
|---|---|---|
| Banco de dados | PostgreSQL | MongoDB |
| Hash de senha | BCrypt | Argon2 |
| Token | JWT | Opaque (Redis) |
| Logger | Console | File |

> Todas as camadas são intercambiáveis via injeção de dependência.

---

## Como Executar

```bash
# Clone o repositório
git clone https://github.com/davioliveiraes/python-projects.git
cd python-projects/py_SOLID_challenge/5_D_DIP

# Execute
python main.py
```

Nenhuma dependência externa necessária. Python 3.10+.

---

## Estrutura

```
dip_auth/
│
├── interfaces/          # Abstrações (contratos)
│   ├── UserRepositoryInterface
│   ├── PasswordHasherInterface
│   ├── TokenServiceInterface
│   └── AuthLoggerInterface
│
├── implementations/     # Implementações concretas
│   ├── repositories/    # PostgresUserRepository, MongoUserRepository
│   ├── hashers/         # BCryptPasswordHasher, Argon2PasswordHasher
│   ├── tokens/          # JWTTokenService, OpaqueTokenService
│   └── loggers/         # ConsoleAuthLogger, FileAuthLogger
│
└── services/
    └── AuthenticationService   # Módulo de alto nível
```

---

## Interfaces Definidas

```python
class UserRepositoryInterface(ABC):
    def save(self, user_data: dict) -> dict: ...
    def find_by_email(self, email: str) -> Optional[dict]: ...
    def update(self, email: str, user_data: dict) -> dict: ...

class PasswordHasherInterface(ABC):
    def hash(self, password: str) -> str: ...
    def verify(self, password: str, hashed: str) -> bool: ...

class TokenServiceInterface(ABC):
    def generate_token(self, user_data: dict) -> str: ...
    def validate_token(self, token: str) -> Optional[dict]: ...
    def revoke_token(self, token: str) -> bool: ...

class AuthLoggerInterface(ABC):
    def log_success(self, email: str, action: str) -> None: ...
    def log_failure(self, email: str, action: str, reason: str) -> None: ...
```

---

## Conceitos DIP

```
❌ Sem DIP                      ✅ Com DIP

AuthService                     AuthService
  └── PostgresRepository          └── UserRepositoryInterface ←── PostgresRepository
  └── BCryptHasher                └── PasswordHasherInterface ←── BCryptHasher
  └── JWTService                  └── TokenServiceInterface   ←── JWTService
  └── ConsoleLogger               └── AuthLoggerInterface     ←── ConsoleLogger
```

> *"Dependa de abstrações, não de implementações concretas."*

O `AuthenticationService` recebe suas dependências via **injeção por construtor**, sem saber qual implementação está sendo usada.

---

## Aprendizados

- Como usar `ABC` e `@abstractmethod` para definir contratos em Python
- A diferença entre acoplamento forte e inversão de dependência
- Como a injeção de dependência viabiliza o DIP na prática
- Que trocar uma implementação (ex: BCrypt → Argon2) não exige nenhuma alteração no serviço de alto nível
- Como o DIP facilita testes unitários com mocks

---

## Autor

**Davi Oliveira - Software Engineer**  

---
