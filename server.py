from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db, Inventory, Warehouse
from datetime import datetime
import crud

# configure a Jinja2 setting to make it throw errors for undefined variables
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def homepage():
    """Homepage - Displays all Warehouses and all inventory"""

    warehouses = Warehouse.query.all()
    inventories = Inventory.query.all()
    return render_template('homepage.html', 
                            warehouses = warehouses, 
                            inventories = inventories)



@app.route('/new_warehouse_form')
def new_warehouse_form():
    """Add a warehouse to the database"""


    return render_template('newWarehouseForm.html')

@app.route('/add_warehouse', methods = ["POST"])
def button_to_add_warehouse():
    """Add a warehouse to the database"""

    location = request.form.get("warehouse_location")
    now = datetime.now()
    created_at = now.strftime("%Y-%b-%d %H:%M:%S")
    updated_at = created_at
    warehouse = crud.create_warehouse(location = location ,created_at= created_at, updated_at = updated_at) #call the helper function in crud.py to create a warehouse
  

    return redirect('/')


@app.route('/new_inventory_form')
def new_inventory_form():
    """Add inventory to the database"""

    warehouses =  Warehouse.query.all()

    return render_template('newInventoryForm.html', warehouses = warehouses)



@app.route('/add_inventory', methods = ["POST"])
def button_to_add_inventory():
    """Add inventory to the database"""

    warehouses =  Warehouse.query.all()
    now = datetime.now()
    created_at = now.strftime("%Y-%b-%d %H:%M:%S")
    updated_at = created_at
    inventory_item = request.form.get("inventory_item")
    quantity = request.form.get("quantity")
    manufacturer = request.form.get("manufacturer")
    comments = request.form.get("comments")
    warehouse_id = request.form.get("warehouse_id")
    
    if crud.validate_inventory(warehouse_id, inventory_item, quantity, manufacturer, created_at, updated_at, comments) is True:
        inventory = crud.create_inventory(warehouse_id = warehouse_id, inventory_item = inventory_item, quantity = quantity, manufacturer = manufacturer, created_at = created_at, updated_at = updated_at, comments = comments) #call the helper function in crud.py to create inventory
        db.session.add(inventory)
        db.session.commit()
        flash("Inventory Added")

        return redirect('/')
    
    else:
        flash("Please make sure all entries are filled and Quantity is in digits only")
        return render_template('newInventoryForm.html', warehouses = warehouses)

       

@app.route('/warehouses/<warehouse_id>', methods = ["GET"])
def show_warehouse_details(warehouse_id):
    """Show all the inventory in a selected warehouse"""

    warehouse = crud.get_warehouse_by_id(warehouse_id)

    return render_template('warehouse_details.html', warehouse = warehouse)



@app.route("/update_inventory/<inventory_id>", methods=["GET", "POST"])
def update_inventory(inventory_id):
    """Allows user to update an existing inventory item"""
    
    now = datetime.now()
    created_at = now.strftime("%Y-%b-%d %H:%M:%S")
    updated_at = created_at
    inventory_to_update = Inventory.query.filter_by(inventory_id=inventory_id).first()
    warehouses = Warehouse.query.all()
   
    if request.method == "POST":
        #update_at timestamp corrected to match the time inventory is updated
        now = datetime.now()
        inventory_to_update.updated_at = now.strftime("%Y-%b-%d %H:%M:%S")
        inventory_to_update.inventory_item = request.form.get('inventory_item')
        inventory_to_update.manufacturer = request.form.get('manufacturer')
        inventory_to_update.quantity = request.form.get('quantity')
        inventory_to_update.comments = request.form.get('comments')
        # Check if the user entered a new warehouse
        if request.form.get('new_warehouse'):
            location = request.form.get('new_warehouse')
            warehouse = crud.create_warehouse(location = location ,created_at= created_at, updated_at = updated_at )
            db.session.add(warehouse)
            inventory_to_update.warehouse_id = warehouse.warehouse_id
        else:
            inventory_to_update.warehouse_id = request.form.get('warehouse_id')
        
        #commit changes to the database
        db.session.add(inventory_to_update)
        db.session.commit()
        flash("Inventory Updated!")
        return redirect('/')

    else:
        return render_template('update_inventory.html', 
                            inventory_to_update = inventory_to_update, 
                            warehouses = warehouses)
                        

@app.route("/delete_inventory/<int:inventory_id>", methods=["POST"])
def delete_inventory(inventory_id):
    """Allows user to delete an existing inventory item"""
    
    item = Inventory.query.filter_by(inventory_id=inventory_id).first()

    #commit delete to the database   
    db.session.delete(item)
    db.session.commit()
    flash("inventory deleted")   
           
    return redirect("/")




if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
