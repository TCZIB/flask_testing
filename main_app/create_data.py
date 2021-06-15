from app import db, Customer, Products, Orders, Order_Contents

db.drop_all()
db.create_all()

user_1 = Customer(first_name="Tommy", last_name="Calvin")

product_1 = Products(name="Shampoo", price=1)
product_2 = Products(name="Conditioner", price=2)

db.session.add(user_1)
db.session.add(product_1)

db.session.commit()

user_1_order = Orders(customer_id=user_1.customer_id)

db.session.add(user_1_order)

db.session.commit()

order_content = Order_Contents(product_id=1, order_id=user_1_order.order_id)
db.session.add(order_content)

order_content = Order_Contents(product_id=2, order_id=user_1_order.order_id)
db.session.add(order_content)

db.session.commit()

