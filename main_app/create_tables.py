from app import db

db.drop_all()
db.create_all()

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    order = db.relationship('Orders', backref='Game')

class Game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Interger, nullable=False)
    customer = db.relationship('Order', backref='Customer')

class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Interger, db.ForeignKey('customer.customer_id'))
    game_id = db.Column(db.Interger), db.ForeignKey('game.game_id'))

db.session.commit()