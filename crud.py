"""CRUD operations."""

from model import db, Inventory, Warehouse, connect_to_db

def create_inventory(inventory_item, quantity, manufacturer, created_at, updated_at, comments):
    """Create and return a new Inventory."""

    inventory = Inventory(inventory_item =inventory_item, quantity = quantity, manufacturer = manufacturer, created_at = created_at, updated_at = updated_at, comments = comments)

    db.session.add(inventory)
    db.session.commit()

    return inventory

def create_warehouse(location,created_at, updated_at):
    """Create and return a new Warehouse"""

    warehouse = Warehouse( location = location, created_at = created_at, updated_at = updated_at)

    db.session.add(warehouse)
    db.session.commit()

    return warehouse

# def update_inventory()


def display_inventory():
    """Display all inventory"""

    return Inventory.query.all()

def display_warehouses():
    """Display all warehouses"""

    return Warehouse.query.all()

def get_warehouse_by_id():

def get_inventory_by_warehouse_id(warehouse_id):
    """Get inventory by warehouse"""

    return Inventory.query.get(warehouse_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)