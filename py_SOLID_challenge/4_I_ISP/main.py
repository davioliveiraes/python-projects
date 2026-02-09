from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

# Interface BASE - apenas o essencial que todos os veículos têm
class VehicleInterface(ABC):

    @abstractmethod
    def start_delivery(self, origin: str, destination: str, distance_km: float) -> dict:
        pass

    @abstractmethod
    def calculate_cost(self, distance_km: float, weight_kg: float) -> float:
        pass

# Interfaces SEGREGADAS - cada uma com responsabilidade específica
class FuelableInterface(ABC):
    """Veículos que usa combustível"""

    @abstractmethod
    def refuel(self, listers: float) -> dict:
        pass

    @abstractmethod
    def get_fuel_level(self) -> float:
        pass

class ElectricInterface(ABC):
    """Veículos elétricos"""

    @abstractmethod
    def recharge_battery(self, percentage: float) -> dict:
        pass

    @abstractmethod
    def get_battery_level(self) -> float:
        pass

class CargoCapableInterface(ABC):
    """Veículos que transportam cargas grandes"""

    @abstractmethod
    def load_cargo(self, weight_kg: float, volume_m3: float) -> dict:
        pass

    @abstractmethod
    def unload_cargo(self) -> dict:
        pass

    @abstractmethod
    def get_cargo_capacity(self) -> dict:
        pass


class RefrigeratedInterface(ABC):
    """Veículos com sistema de refrigeração"""

    @abstractmethod
    def enable_refrigeration(self, temperature: float) -> dict:
        pass

    @abstractmethod
    def disable_refrigeration(self) -> dict:
        pass
    
    @abstractmethod
    def get_current_temperature(self) -> float:
        pass

class GPSTrackableInterface(ABC):
    """Veículos com GPS"""

    @abstractmethod
    def track_gps_location(self) -> dict:
        pass

    @abstractmethod
    def get_route_history(self) -> list:
        pass

class HeavyMaintenanceInterface(ABC):

    @abstractmethod
    def schedule_maintenance(self, date: datetime, service_type: str) -> dict:
        pass

    @abstractmethod
    def get_maintenance_history(self) -> list:
        pass       

class TireCheckInterface(ABC):

    @abstractmethod
    def check_tire_pressure(self) -> dict:
        pass

    @abstractmethod
    def adjust_tire_pressure(self, tire: str, pressure: float) -> dict:
        pass

class AirSuspensionInterface(ABC):
    
    @abstractmethod
    def activate_air_suspesion(self) -> dict:
        pass

    @abstractmethod
    def adjust_suspension_height(self, height_cm: float) -> dict:
        pass

# Moto - implementa APENAS as interfaces que fazem sentido
class Motorcyle(VehicleInterface, FuelableInterface, TireCheckInterface):

    def __init__(self, plate: str, driver: str):
        self.plate = plate
        self.driver = driver
        self.fuel_tank = 15.0
        self.current_fuel = 15.0
    
    # VehicleInterface
    def start_delivery(self, origin: str, destination: str, distance_km: float) -> dict:
        return {
            "status": "sucesso",
            "veiculo": "motocicleta",
            "placa": self.plate,
            "rota": f"{origin} -> {destination}",
            "distance": distance_km
        }
    
    def calculate_cost(self, distance_km: float, weight_kg: float) -> float:
        return distance_km * 2.50
    
    # FuelableInterface
    def refuel(self, liters: float) -> dict:
        self.current_fuel = min(self.fuel_tank, self.current_fuel + liters)
        return {"status": "sucesso", "nivel_de_combustivel": self.current_fuel}
    
    def get_fuel_level(self) -> float:
        return self.current_fuel
    
    # TireCheckInterface
    def check_tire_pressure(self) -> dict:
        return {"dianteiro": 32, "traseiro": 36}
    
    def adjust_tire_pressure(self, tire: str, pressure: float) -> dict:
        return {"status": "sucesso", "pneu": tire, "pressao": pressure}

# Caminhão Refrigerado - implementa MUITAS interfaces (veículo complexo)
class RefrigeratedTruck(
    VehicleInterface,
    FuelableInterface,
    CargoCapableInterface,
    RefrigeratedInterface,
    GPSTrackableInterface,
    HeavyMaintenanceInterface,
    TireCheckInterface,
    AirSuspensionInterface
):
    def __init__(self, plate: str, driver: str):
        self.plate = plate
        self.driver = driver
        self.fuel_tank = 300.0
        self.current_fuel = 300.0
        self.refrigeration_on = False
        self.temperature = 25.0
        self.cargo_weight = 0.0
        self.cargo_volume = 0.0
        self.max_cargo_weight = 10000.0
        self.max_cargo_volume = 50.0
    
    # VehicleInterface
    def start_delivery(self, origin: str, destination: str, distance_km: float) -> dict:
        return {
            "status": "sucesso",
            "veiculo": "tanque_refrigerador",
            "placa": self.plate,
            "rota": f"{origin} -> {destination}",
            "distancia": distance_km,
            "refrigeracao": self.refrigeration_on
        }
    
    def calculate_cost(self, distance_km: float, weight_kg: float) -> float:
        base_cost = distance_km * 8.50 + weight_kg * 0.50
        refrigeration_cost = distance_km * 2.00 if self.refrigeration_on else 0
        return base_cost + refrigeration_cost
    
    # FuelableInterface
    def refuel(self, liters: float) -> dict:
        self.current_fuel = min(self.fuel_tank, self.current_fuel + liters)
        return {"status": "sucesso", "nivel_de_combustivel": self.current_fuel}
    
    def get_fuel_level(self) -> float:
        return self.current_fuel
    
    # CargoCapableInterface
    def load_cargo(self, weight_kg: float, volume_m3: float) -> dict:
        if weight_kg > self.max_cargo_weight:
            return {"status": "error", "messagem": "capacidade_de_peso_excedida"}
        if volume_m3 > self.max_cargo_weight:
            return {"status": "sucesso", "peso": weight_kg, "volume": volume_m3}
        
        self.cargo_weight = weight_kg
        self.cargo_volume = volume_m3
        return {"status": "sucesso", "peso": weight_kg, "volume": volume_m3}
    
    def unload_cargo(self) -> dict:
        weight = self.cargo_weight
        volume = self.cargo_volume
        self.cargo_weight = 0.0
        self.cargo_volume = 0.0
        return {"status": "sucesso", "peso_descarregado": weight, "volume_descarregado": volume}
    
    def get_cargo_capacity(self) -> dict:
        return {
            "peso_maxima": self.max_cargo_weight,
            "volume_maximo": self.max_cargo_volume,
            "peso_atual": self.cargo_weight,
            "volume_atual": self.cargo_volume
        }
    
    # RefrigeratedInterface
    def enable_refrigeration(self, temperature: float) -> dict:
        self.refrigeration_on = True
        self.temperature = temperature
        return {"status": "ativar", "temperatura": temperature}

    def disable_refrigeration(self) -> dict:
        self.refrigeration_on = False
        self.temperature = 25.0
        return {"status": "desativar"}

    def get_current_temperature(self) -> float:
        return self.temperature 
    
    # GPSTrackableInterface
    def track_gps_location(self) -> dict:
        return {"latitude": -23.550520, "longitude": -46.633308, "data_e_hora": datetime.now()}
    
    def get_route_history(self) -> list:
        return [
            {"latitude": -23.550520, "longitude": -46.633308, "hora": "10:00"},
            {"latitude": -23.560520, "longitude": -46.643308, "hora": "10:30"}
        ]
    
    # HeavyMaintenanceInterface
    def schedule_maintenance(self, date: datetime, service_type: str) -> dict:
        return {"status": "agendamento", "data": date, "servico": service_type}
    
    def get_maintenance_history(self) -> list:
        return [
            {"data": "2026-01-15", "servico": "troca_de_oleo"},
            {"data": "2025-12-10", "servico": "inspecao_de_freios"}
        ]

    # TireCheckInterface
    def check_tire_pressure(self) -> dict:
        return {
            "dianteiro_esquerdo": 110,
            "dianteiro_direito": 110,
            "traseiro_esquerdo": 110,
            "traseiro_esquerdo": 110
        }
    
    def adjust_tire_pressure(self, tire: str, pressure: float) -> dict:
        return {"status": "sucesso", "pneu": tire, "pressao": pressure}
    
    # AirSuspensionInterface
    def activate_air_suspesion(self) -> dict:
        return {"status": "ativada", "modo": "comforto"}
    
    def adjust_suspension_height(self, height_cm: float) -> dict:
        return {"status": "ajustado", "altura": height_cm}

# DRONE - implementa APENAS as interface que fazem sentido
class DeliveryDrone(VehicleInterface, ElectricInterface, GPSTrackableInterface):

    def __init__(self, serial: str):
        self.serial = serial
        self.battery_level = 100.0
        self.max_battery = 100.0
    
    # VehicleInterface
    def start_delivery(self, origin: str, destination: str, distance_km: float) -> dict:
        return {
            "status": "sucesso",
            "veiculo": "Drone",
            "serial": self.serial,
            "rota": f"{origin} -> {destination}",
            "distancia": distance_km,
            "eta_minutos": distance_km * 2
        }
    
    def calculate_cost(self, distance_km: float, weight_kg: float) -> float:
        return distance_km * 5.00 + weight_kg * 2.00
    
    # ElectricInterface
    def recharge_battery(self, percentage: float) -> dict:
        return {"status": "sucesso", "nivel_da_bateria": self.battery_level}
    
    def get_battery_level(self) -> float:
        return self.battery_level
    
    # GPSTrackableInterface
    def track_gps_location(self) -> dict:
        return {
            "latitude": -23.550520,
            "longitude": -46.633308,
            "altitude": 150,
            "data_e_hora": datetime.now()
        }
    
    def get_route_history(self) -> list:
        return [
            {"latitude": -23.550520, "longitude": -46.633308, "altitude": 150, "hora": "11:00"},
            {"latitude": -23.555520, "longitude": -46.638308, "altitude": 155, "hora": "11:05"}
        ]
    
# BICLETA ELÉTRICA - implementa APENAS as interfaces que fazem sentido
class ElectricBicycle(VehicleInterface, ElectricInterface, TireCheckInterface):

    def __init__(self, plate: str, driver: str):
        self.plate = plate
        self.driver = driver
        self.battery_level = 100.0
        self.max_battery = 100.0
    
    # VehicleInterface
    def start_delivery(self, origin: str, destination: str, distance_km: float) -> dict:
        return {
            "status": "sucesso",
            "veiculo": "Bicicleta Eletrica",
            "placa": self.plate,
            "rota": f"{origin} -> {destination}",
            "distancia": distance_km,
            "ecologicamente_correto": True
        }
    
    def calculate_cost(self, distance_km: float, weight_kg: float) -> float:
        return distance_km * 1.50
    
    # ElectriInterface
    def recharge_battery(self, percentage: float) -> dict:
        self.battery_level = min(self.max_battery, self.battery_level + percentage)
        return {"status": "sucesso", "nivel_da_bateria": self.battery_level}
    
    def get_battery_level(self) -> float:
        return self.battery_level
    
    # TireCheckInterface
    def check_tire_pressure(self) -> dict:
        return {"dianteiro": 45, "traseiro": 45}
    
    def adjust_tire_pressure(self, tire: str, pressure: float) -> dict:
        return {"status": "sucesso", "pneu": tire, "presao": pressure}
    
# Sistema que usa o verificação de tipo(TypeChecking) para verificar capacidades
class FleetManager:

    def prepare_vehicle_for_delivery(self, vehicle: VehicleInterface, cargo_weight: float = 0) -> dict:
        """Pepara o veículo baseado nas suas capacidades"""
        preparations = []

        # Verifica se precisa abastecer
        if isinstance(vehicle, FuelableInterface):
            if vehicle.get_fuel_level() < 10:
                vehicle.refuel(50)
                preparations.append("Refueled")
        
        # Verifica se precisa recarregar
        if isinstance(vehicle, ElectricInterface):
            if vehicle.get_battery_level() < 20:
                vehicle.recharge_battery
                preparations.append("Bateria recarregada")
        
        # Verifica se tem carga
        if isinstance(vehicle, CargoCapableInterface) and cargo_weight > 0:
            vehicle.load_cargo(cargo_weight, cargo_weight * 0.001)
            preparations.append(f"Carga Carregada: {cargo_weight}kg")
        
        # Verifica pressão dos pneus
        if isinstance(vehicle, TireCheckInterface):
            pressures = vehicle.check_tire_pressure()
            preparations.append(f"Pneus verificados: {pressures}")
        
        # Ativa GPS se disponível
        if isinstance(vehicle, GPSTrackableInterface):
            location = vehicle.track_gps_location()
            preparations.append(f"GPS ativo: {location['latitude']}, {location['longitude']}")
        
        return {"status": "preparar", "preparations": preparations}

    def handle_refrigerated_delivery(self, vehicle: VehicleInterface, temperature: float) -> dict:
        if not isinstance(vehicle, RefrigeratedInterface):
            return {"status": "error", "mensagem": "O veículo não suporta refrigeração"}
        
        vehicle.enable_refrigeration(temperature)
        return {"status": "sucesso", "mensagem": f"Refrigeração habilitada em {temperature}°C"}

# Exemplo de Uso
if __name__ == "__main__":
    manager = FleetManager()

    print("==MOTO==")
    moto = Motorcyle("ADS-1233", "Naruto")
    print(manager.prepare_vehicle_for_delivery(moto))
    print(moto.start_delivery("Loja A", "Casa B", 10))

    print("\n==CAMINHÃO REFRIGERADO==")
    truck = RefrigeratedTruck("XCZ-1232", "Sasuke")
    print(manager.prepare_vehicle_for_delivery(truck, cargo_weight=500))
    print(manager.handle_refrigerated_delivery(truck, temperature=-18))

    print("\n==DRONE==")
    drone = DeliveryDrone("DNS-002")
    print(manager.prepare_vehicle_for_delivery(drone))
    print(drone.start_delivery("Farmacia", "Cliente", 10))

    print("\n==BICICLETA ELÉTRICA==")
    bike = ElectricBicycle("BKS-7777", "Sakura")
    print(manager.prepare_vehicle_for_delivery(bike))
    print(bike.start_delivery("Restaurante", "Apartamento", 3))

    print("\n=== TESTE: Refrigeração em Moto ===")
    print(manager.handle_refrigerated_delivery(moto, temperature=-18))

