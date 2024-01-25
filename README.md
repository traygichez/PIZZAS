# Pizza Restaurants API

This is a simple Flask API for managing pizza restaurants, pizzas, and their prices.

## Prerequisites

Make sure you have the following installed before running the application:

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Flask CORS

Install the dependencies using the following command:

```bash
pip install -r requirements.txt
Setup
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/your-repository.git
cd your-repository
Initialize the database and seed initial data:
bash
Copy code
python seed.py
Usage
Run the Flask application:
bash
Copy code
python app.py
The API will be accessible at http://127.0.0.1:5555/.

Endpoints
GET /restaurants: Get a list of all restaurants.

GET /restaurants/{id}: Get details of a specific restaurant by ID.

DELETE /restaurants/{id}: Delete a restaurant by ID.

GET /pizzas: Get a list of all pizzas.

POST /restaurant_pizzas: Create a new RestaurantPizza entry.

Models
Restaurant

Fields: id, name, address
Relationship: restaurant_pizzas
Pizza

Fields: id, name, ingredients
Relationship: restaurant_pizzas
RestaurantPizza

Fields: id, pizza_id, restaurant_id, price
Relationships: restaurant, pizza
# author
ONESIMUS GITHUA
