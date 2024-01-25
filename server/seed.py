from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-SQLAlchemy
db.init_app(app)

# Push an application context to make database operations work
with app.app_context():
    print("Deleting data...")
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    print("Creating restaurants...")
    pizzeria1 = Restaurant(name="Mike's Pizza Paradise", address='123 Main St')
    pizzeria2 = Restaurant(name="Sara's Pizza Oasis", address='456 Oak Ave')
    pizzeria3 = Restaurant(name="Alex's Pizza Junction", address='789 Pine Rd')
    pizzeria4 = Restaurant(name="Emily's Pizza Corner", address='101 Elm St')
    pizzeria5 = Restaurant(name="Chris's Pizza Haven", address='202 Maple Ave')
    pizzeria6 = Restaurant(name="Julia's Pizza Palace", address='303 Cedar Rd')
    pizzeria7 = Restaurant(name="Mark's Pizza World", address='404 Birch St')
    pizzeria8 = Restaurant(name="Lily's Pizza Delight", address='505 Pine Ave')
    pizzeria9 = Restaurant(name="Daniel's Pizza Kingdom", address='606 Oak Rd')
    pizzeria10 = Restaurant(name="Sophie's Pizza Express", address='707 Elm Ave')
    
    pizzerias = [pizzeria1, pizzeria2, pizzeria3, pizzeria4, pizzeria5, pizzeria6, pizzeria7, pizzeria8, pizzeria9, pizzeria10]

    print("Creating pizzas...")
    margherita = Pizza(name="Classic Margherita", ingredients="Dough, Tomato Sauce, Cheese, Basil")
    veggie_supreme = Pizza(name="Vegetarian Supreme", ingredients="Dough, Tomato Sauce, Cheese, Mushrooms, Bell Peppers, Olives")
    meat_lovers = Pizza(name="Ultimate Meat Lovers", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni, Sausage, Bacon")
    hawaiian = Pizza(name="Hawaiian Delight", ingredients="Dough, Tomato Sauce, Cheese, Ham, Pineapple")
    bbq_chicken = Pizza(name="BBQ Chicken Feast", ingredients="Dough, BBQ Sauce, Cheese, Chicken, Red Onion, Cilantro")
    supreme = Pizza(name="Supreme Extravaganza", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni, Sausage, Mushrooms, Onions, Bell Peppers")
    vegetarian = Pizza(name="Ultimate Vegetarian", ingredients="Dough, Tomato Sauce, Cheese, Spinach, Artichokes, Sun-dried Tomatoes")
    seafood_delight = Pizza(name="Seafood Delight", ingredients="Dough, White Sauce, Cheese, Shrimp, Crab, Garlic")
    spicy_diablo = Pizza(name="Spicy Diablo", ingredients="Dough, Tomato Sauce, Cheese, Spicy Sausage, Jalapeños, Red Peppers")
    four_cheese = Pizza(name="Four Cheese Delight", ingredients="Dough, Tomato Sauce, Mozzarella, Cheddar, Parmesan, Feta")
    
    pizzas = [margherita, veggie_supreme, meat_lovers, hawaiian, bbq_chicken, supreme, vegetarian, seafood_delight, spicy_diablo, four_cheese]

    print("Creating RestaurantPizza...")
    pr1 = RestaurantPizza(restaurant=pizzeria1, pizza=margherita, price=12)
    pr2 = RestaurantPizza(restaurant=pizzeria2, pizza=veggie_supreme, price=15)
    pr3 = RestaurantPizza(restaurant=pizzeria3, pizza=meat_lovers, price=18)
    pr4 = RestaurantPizza(restaurant=pizzeria4, pizza=hawaiian, price=14)
    pr5 = RestaurantPizza(restaurant=pizzeria5, pizza=bbq_chicken, price=16)
    pr6 = RestaurantPizza(restaurant=pizzeria6, pizza=supreme, price=20)
    pr7 = RestaurantPizza(restaurant=pizzeria7, pizza=vegetarian, price=22)
    pr8 = RestaurantPizza(restaurant=pizzeria8, pizza=seafood_delight, price=25)
    pr9 = RestaurantPizza(restaurant=pizzeria9, pizza=spicy_diablo, price=18)
    pr10 = RestaurantPizza(restaurant=pizzeria10, pizza=four_cheese, price=21)
    
    restaurantPizzas = [pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10]

    # Add all instances to the database
    db.session.add_all(pizzerias)
    db.session.add_all(pizzas)
    db.session.add_all(restaurantPizzas)

    # Commit the changes
    db.session.commit()

    print("Seeding done!")
