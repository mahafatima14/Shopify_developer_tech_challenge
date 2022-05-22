"""Data to populate test db."""

from model import Inventory, Warehouse, db
from datetime import datetime

def example_data():
    """Creating some sample data."""
    
    # In case this is run more than once, empty out existing data
    Inventory.query.delete()
    Warehouse.query.delete()

    # Add sample warehouses
    W1 = Warehouse(location = "Dublin", created_at = datetime.now(), updated_at = datetime.now())
    W2 = Warehouse(location = "Antioch", created_at = datetime.now(), updated_at = datetime.now())
    W3 = Warehouse( location = "Waterloo", created_at = datetime.now(), updated_at = datetime.now())

    # Add sample inventory
    first_inventory = Inventory(warehouse_id = 1, inventory_item = "Sofa", quantity = 18, manufacturer = "Lowes", created_at = datetime.now(), updated_at = datetime.now(), comments = "Pearl White - Handle with care" )
    second_inventory = Inventory(warehouse_id = 2, inventory_item = "Mattress", quantity = 10, manufacturer = "Kholes", created_at = datetime.now(), updated_at = datetime.now(), comments = "" )
    

    db.session.add_all([W1, W2, W3, first_inventory, second_inventory])
    db.session.commit()