"""seeding data into our database"""
import os
from datetime import datetime

import crud
import model
import server

os.system("dropdb inventory")
os.system("createdb inventory")
 
model.connect_to_db(server.app)
model.db.create_all()

model.connect_to_db(server.app) 
model.db.create_all()

# def load_customers():
#     """Customers"""
#     #seed the first user in the database and add to the session:
#     first_customer = model.Customer(name = "Ron Weasley", email = "test1@test.test", address = "123 Taylor Way", phone_number = "12345678")
#     model.db.session.add(first_customer)

#     #seed the second user to the database and add to the session:
#     second_customer= model.Customer(name = "Harry Potter", email = "test2@test.test", address = "123 David Way", phone_number = "12345676")
#     model.db.session.add(second_customer)

#     third_customer= model.Customer(name = "Hermoine G", email = "test3@test.test", address = "123 Ally Way", phone_number = "12345679")
#     model.db.session.add(third_customer)

#     #commit users to the database
#     model.db.session.commit()


# load_customers()

def load_warehouses():
    """Sample data for warehouses"""


    #seed the first inventory in the database and add to the session:
    first_warehouse = model.Warehouse( location = "Dublin", created_at = datetime.now(), updated_at = datetime.now())
    model.db.session.add(first_warehouse)
    
    second_inventory = model.Warehouse( location = "Antioch", created_at = datetime.now(), updated_at = datetime.now())
    model.db.session.add(second_inventory)
    
    

    #commit warehouses to the database
    model.db.session.commit()

load_warehouses() 

def load_inventory():
    """Sample data for inventory"""


    #seed the first inventory in the database and add to the session:
    first_inventory = model.Inventory(warehouse_id = 1, inventory_item = "Sofa", quantity = 18, manufacturer = "Lowes", created_at = datetime.now(), updated_at = datetime.now(), comments = "Pearl White - Handle with care" )
    model.db.session.add(first_inventory)
    
    second_inventory = model.Inventory(warehouse_id = 2, inventory_item = "Mattress", quantity = 10, manufacturer = "Kholes", created_at = datetime.now(), updated_at = datetime.now(), comments = "" )
    model.db.session.add(second_inventory)
    
    

    #commit inventories to the database
    model.db.session.commit()

load_inventory()   

  

