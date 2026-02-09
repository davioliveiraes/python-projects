# Sistema de Frota de Entregas — Interface Segregation Principle (ISP)

## Sobre o Projeto

Sistema de gerenciamento de frota de entregas que demonstra a aplicação do **Princípio de Segregação de Interfaces (ISP)** do SOLID. O projeto modela diferentes tipos de veículos — motocicleta, caminhão refrigerado, drone e bicicleta elétrica — onde cada veículo implementa **apenas** as interfaces que fazem sentido para suas capacidades reais.

Em vez de forçar todos os veículos a implementar uma única interface gigante com métodos que não utilizam, o sistema divide as responsabilidades em **interfaces pequenas e específicas**, permitindo composição flexível.

---

## Benefícios do ISP

- **Sem implementações vazias**: nenhum veículo é obrigado a implementar métodos que não usa
- **Alta coesão**: cada interface tem uma responsabilidade clara e bem definida
- **Facilidade de extensão**: novos veículos podem ser criados combinando apenas as interfaces necessárias
- **Menor acoplamento**: alterações em uma interface não afetam veículos que não a utilizam
- **Código mais limpo**: classes menores, mais legíveis e mais fáceis de testar
- **Composição sobre herança**: veículos são compostos por capacidades, não por hierarquias rígidas

---

## Funcionalidades

- **Iniciar entregas** com origem, destino e distância
- **Calcular custos** de entrega por veículo
- **Abastecer** veículos a combustível ou **recarregar** veículos elétricos
- **Carregar e descarregar** cargas em veículos compatíveis
- **Ativar refrigeração** em veículos com sistema refrigerado
- **Rastrear GPS** em veículos com rastreamento
- **Verificar e ajustar pressão dos pneus**
- **Agendar manutenção** para veículos pesados
- **Ajustar suspensão a ar** em veículos compatíveis
- **Gerenciamento inteligente da frota** com verificação dinâmica de capacidades via `isinstance()`

---

## Tecnologias

- **Python 3.10+**
- **ABC (Abstract Base Classes)** — para definição de interfaces abstratas
- **Type Checking** — verificação dinâmica de capacidades com `isinstance()`
- **Tipagem estática** — uso de type hints para clareza do código

---

## Como Executar

```bash
# Clone o repositório
git clone https://github.com/davioliveiraes/python-projects.git

# Acesse o diretório
cd python-projects/py_SOLID_challenge/4_I_ISP

# Execute o projeto
python main.py
```

**Saída esperada:**

```
==MOTO==
{'status': 'preparar', 'preparations': [...]}
{'status': 'sucesso', 'veiculo': 'motocicleta', ...}

==CAMINHÃO REFRIGERADO==
{'status': 'preparar', 'preparations': [...]}
{'status': 'sucesso', 'mensagem': 'Refrigeração habilitada em -18°C'}

==DRONE==
{'status': 'preparar', 'preparations': [...]}
{'status': 'sucesso', 'veiculo': 'Drone', ...}

==BICICLETA ELÉTRICA==
{'status': 'preparar', 'preparations': [...]}
{'status': 'sucesso', 'veiculo': 'Bicicleta Eletrica', ...}

=== TESTE: Refrigeração em Moto ===
{'status': 'error', 'mensagem': 'O veículo não suporta refrigeração'}
```

---

## 📁 Estrutura

```
4_I_ISP/
├── main.py          # Código principal com interfaces, veículos e gerenciador
└── README.md        # Documentação do projeto
```

### Interfaces Definidas

| Interface | Responsabilidade |
|---|---|
| `VehicleInterface` | Operações base: iniciar entrega e calcular custo |
| `FuelableInterface` | Abastecer e verificar nível de combustível |
| `ElectricInterface` | Recarregar e verificar nível de bateria |
| `CargoCapableInterface` | Carregar, descarregar e consultar capacidade de carga |
| `RefrigeratedInterface` | Ativar/desativar refrigeração e consultar temperatura |
| `GPSTrackableInterface` | Rastrear localização e histórico de rotas |
| `HeavyMaintenanceInterface` | Agendar e consultar histórico de manutenção |
| `TireCheckInterface` | Verificar e ajustar pressão dos pneus |
| `AirSuspensionInterface` | Ativar e ajustar suspensão a ar |

### Mapa de Veículos x Interfaces

| Veículo | Vehicle | Fuel | Electric | Cargo | Refrigerated | GPS | Maintenance | Tire | Suspension |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Motorcycle | ✅ | ✅ | — | — | — | — | — | ✅ | — |
| RefrigeratedTruck | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| DeliveryDrone | ✅ | — | ✅ | — | — | ✅ | — | — | — |
| ElectricBicycle | ✅ | — | ✅ | — | — | — | — | ✅ | — |

---

## Conceito ISP

O **Interface Segregation Principle** afirma:

> *"Nenhum cliente deve ser forçado a depender de métodos que não utiliza."*

### ❌ Violação do ISP

Sem o ISP, teríamos uma **interface monolítica** forçando todos os veículos a implementar tudo:

```python
class VehicleInterface(ABC):
    @abstractmethod
    def start_delivery(self, origin, destination, distance_km): ...

    @abstractmethod
    def calculate_cost(self, distance_km, weight_kg): ...

    @abstractmethod
    def refuel(self, liters): ...

    @abstractmethod
    def recharge_battery(self, percentage): ...

    @abstractmethod
    def load_cargo(self, weight_kg, volume_m3): ...

    @abstractmethod
    def enable_refrigeration(self, temperature): ...

    @abstractmethod
    def track_gps_location(self): ...

    @abstractmethod
    def schedule_maintenance(self, date, service_type): ...

    @abstractmethod
    def check_tire_pressure(self): ...

    @abstractmethod
    def activate_air_suspension(self): ...
```

**Problema:** Uma moto seria forçada a implementar `enable_refrigeration()`, `load_cargo()`, `activate_air_suspension()` e outros métodos que **não fazem sentido** para ela:

```python
class Motorcycle(VehicleInterface):
    def enable_refrigeration(self, temperature):
        raise NotImplementedError("Moto não tem refrigeração!")  # 💀

    def load_cargo(self, weight_kg, volume_m3):
        raise NotImplementedError("Moto não transporta carga!")  # 💀

    def activate_air_suspension(self):
        raise NotImplementedError("Moto não tem suspensão a ar!")  # 💀
```

Isso gera **código morto**, **exceções em runtime** e **violação do contrato** da interface.

### ✅ Aplicação Correta do ISP

Com o ISP, as interfaces são **segregadas por responsabilidade**, e cada veículo **compõe apenas o que precisa**:

```python
# Interfaces pequenas e coesas
class VehicleInterface(ABC):        # Base para todos
class FuelableInterface(ABC):       # Combustível
class ElectricInterface(ABC):       # Bateria
class CargoCapableInterface(ABC):   # Carga
class RefrigeratedInterface(ABC):   # Refrigeração
class GPSTrackableInterface(ABC):   # Rastreamento
class TireCheckInterface(ABC):      # Pneus

# Moto implementa APENAS o que faz sentido
class Motorcycle(VehicleInterface, FuelableInterface, TireCheckInterface):
    ...  # Sem métodos mortos!

# Caminhão implementa TUDO que precisa
class RefrigeratedTruck(
    VehicleInterface, FuelableInterface, CargoCapableInterface,
    RefrigeratedInterface, GPSTrackableInterface, HeavyMaintenanceInterface,
    TireCheckInterface, AirSuspensionInterface
):
    ...  # Cada método é relevante!

# Drone: elétrico + GPS, sem pneus ou combustível
class DeliveryDrone(VehicleInterface, ElectricInterface, GPSTrackableInterface):
    ...  # Limpo e coerente!
```

O `FleetManager` usa **verificação de tipo** (`isinstance()`) para lidar com cada capacidade de forma segura e polimórfica, sem precisar saber o tipo concreto do veículo.

---

## Aprendizados

- Como identificar interfaces "gordas" que violam o ISP
- Segregação de interfaces usando **ABC** do Python
- Herança múltipla em Python para composição de interfaces
- Uso de `isinstance()` para verificação dinâmica de capacidades
- Diferença entre **herança de implementação** e **herança de interface**
- Aplicação prática do SOLID em sistemas do mundo real
- Design de sistemas flexíveis e extensíveis

---

## Autor

**Davi Oliveira** — Software Engineer
