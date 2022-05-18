"""Models for Inventory tracking web App; part of Developers Intern Challenge @ Shopify."""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Inventory(db.Model):
    """An Inventory""" 

    __tablename__ = "inventories"  

    inventory_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)   
    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouses.warehouse_id"), nullable = True)
    inventory_item = db.Column(db.String, nullable=False)
    quantity = db.Column(db.String, nullable=False)
    manufacturer = db.Column(db.String, nullable = False, unique = False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    comments = db.Column(db.Text, nullable = True)
    #tracking_code = db.Column(db.String, nullable=False)
    #shipment_status = db.Column(db.Text, nullable=True)
    #transportation_method =  db.Column(db.Text, default=None, nullable=True) (if we wanted to check if the package is being delivered through motor vehicle/airplane?)

    warehouse = db.relationship("Warehouse", backref= "inventory")

    def __repr__(self):
        return f"<Inventory inventory_id={self.inventory_id}>"



class Warehouse(db.Model):
    """The warehouse"""

    __tablename__ = "warehouses"


    warehouse_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
   
    location = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    #capacity = db.Column(db.Integer)
      

    

    def __repr__(self):
        return f"<warehouse warehouse_id={self.warehouse_id} name={self.location}>"


def connect_to_db(flask_app, db_uri="postgresql:///inventory", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)



# class Comment(db.Model):
#     """A customer.""" 

#     __tablename__ = "comments"  

#     comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)
#     inventory_id = db.Column(db.Integer, db.ForeignKey("inventory.inventory_id"), nullable = False)
#     comment = db.Column(db.Text)
#     created_at = db.Column(db.Datetime, nullable=False)
#     updated_at = db.Column(db.Datetime, nullable=False)

#     def __repr__(self):
#         return f"<User user_id={self.customer_id} name={self.name}>"


# class sending_inventory(db.Model):
#     """Inventory dropped off"""

#     __tablename__ = "sending_inventories"

#     sending_inventory_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
#     customer_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)
#     inventory_id = db.Column(db.Integer, db.ForeignKey("inventories.inventory_id"), nullable = False)
#     created_at = db.Column(db.Datetime, nullable=False)

#     customer = db.relationship("Customer", backref= "sending_inventories")
#     inventory = db.relationship("Inventory", backref = "sending_inventories")

#     def __repr__(self):
#         return f"<dropoff_inventory id={self.sending_inventory_id}>"





# class recieving_inventory(db.Model):
#     """Inventory picked up for delivery"""

#     __tablename__ = "recieving_inventories"

#     recieving_inventory_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)
#     inventory_id = db.Column(db.Integer, db.ForeignKey("inventories.inventory_id"), nullable = False)
#     created_at = db.Column(db.Datetime, nullable=False)


#     customer = db.relationship("Customer", backref= "recieving_inventories")
#     inventory = db.relationship("Inventory", backref = "recieving_inventories")


#     def __repr__(self):
#         return f"<pickup_inventory id={self.recieving_inventory_id}>"

