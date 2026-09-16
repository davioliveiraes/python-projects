from src.models.repositories.orders_repository import OrdersRepository
from src.models.connection.connection_handler import db_connection_handler
from src.use_cases.registry_update import RegistryUpdate

def registry_updater_composer():
    conn = db_connection_handler.get_db_connection()
    model = OrdersRepository(conn)
    use_case = RegistryUpdate(model)

    return use_case
