from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # create SQLALchemy object

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    order = db.relationship('Orders', backref='customer')

class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    order_products = db.relationship('Order_Contents', backref='product')

class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))

class Order_Contents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')