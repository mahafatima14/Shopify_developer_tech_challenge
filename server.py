from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
from datetime import datetime
import crud

# configure a Jinja2 setting to make it throw errors for undefined variables
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def homepage():
    """Homepage - Displays all Warehouses and its inventory"""

    warehouses = crud.display_warehouses()
    inventories = crud.display_inventory()
    return render_template('homepage.html', warehouses = warehouses, inventories = inventories)



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
    # inventory_item = request.form.get("inventory_item")
    # quantity = request.form.get("quantity")
    # manufacturer = request.form.get("manufacturer")
    # comments = request.form.get("comments")

    # inventory = crud.create_inventory(inventory_item = inventory_item, quantity = quantity, manufacturer = manufacturer, created_at = created_at, updated_at = updated_at, comments = comments)
    warehouse = crud.create_warehouse(location = location ,created_at= created_at, updated_at = updated_at)

    return redirect('/')

@app.route('/warehouses/<warehouse_id>')
def show_warehouse_details(warehouse_id):
    """Show all the inventory in a selected warehouse"""

    warehouse = crud.get_warehouse_by_id(warehouse_id)

    return render_template('warehouse_details.html', warehouse = warehouse)


@app.route('/addinventory', methods = ['POST'])
def add_inventory():
    """Homepage - Displays all Warehouses and its inventory"""

    warehouses = crud.display_warehouses()
    inventories = crud.display_inventory()
    return render_template('homepage.html', warehouses = warehouses, inventories = inventories)



# @app.route("/inventory/<inventory_id>", methods=["DELETE"])
# def commit_delete():
#     """Allows user to delete an existing inventory item"""
    
#     deleted = request.form.get("deleted")
#     item = Inventory.query.filter_by(name=deleted).first()
#     db.session.delete(item)
#     db.session.commit()
           
#     return redirect("/")



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
