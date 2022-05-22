"""CRUD operation helper functions"""

from model import db, Inventory, Warehouse, connect_to_db

def create_inventory(warehouse_id, inventory_item, quantity, manufacturer, created_at, updated_at, comments):
    """Create and return a new Inventory."""

    inventory = Inventory(warehouse_id = warehouse_id, inventory_item =inventory_item, quantity = quantity, manufacturer = manufacturer, created_at = created_at, updated_at = updated_at, comments = comments)

    db.session.add(inventory)
    db.session.commit()

    return inventory

def create_warehouse(location,created_at, updated_at):
    """Create and return a new Warehouse"""

    warehouse = Warehouse( location = location, created_at = created_at, updated_at = updated_at)

    db.session.add(warehouse)
    db.session.commit()

    return warehouse

def validate_inventory(warehouse_id, inventory_item, quantity, manufacturer, created_at, updated_at, comments):
    """Validate the input in the create inventory form"""

    if  warehouse_id == "" or \
        inventory_item == "" or \
        quantity == "" or \
        manufacturer == "" or \
        not warehouse_id.isdigit() or \
        not quantity.isdigit():
            return False
    else:
        return True


def get_warehouse_by_id(warehouse_id):
    """Get warehouse by id"""

    return Warehouse.query.get(warehouse_id)

def get_inventory_by_id(inventory_id):
    """Get inventory by warehouse"""

    return Inventory.query.get(inventory_id)





if __name__ == '__main__':
    from server import app
    connect_to_db(app)