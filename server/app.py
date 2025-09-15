from flask import Flask, jsonify
from flask_pymongo import PyMongo
# my dear keshav
app = Flask(__name__)

# Configure MongoDB connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
app.config['MONGO_DATABASE'] = 'mydatabase'

# Create a PyMongo instance
mongo = PyMongo(app)

# --- Database Creation and Data Insertion ---

# 1. Create the Database (if it doesn't exist)
try:
    mongo.db.command_find_one({"operation": "create", "db": "mydatabase"})
    print("Database 'mydatabase' already exists.")
except Exception as e:
    print(f"Creating database 'mydatabase': {e}")

# 2. Insert Data into the 'items' collection
if 'items' not in mongo.db.list_collection_names():
    items_data = [
        {"name": "Laptop", "description": "High-performance laptop", "price": 1200},
        {"name": "Mouse", "description": "Wireless mouse", "price": 25},
        {"name": "Keyboard", "description": "Mechanical keyboard", "price": 75}
    ]
    try:
        mongo.db.items.insert_many(items_data)
        print("Data inserted into the 'items' collection.")
    except Exception as e:
        print(f"Error inserting data: {e}")
else:
    print("The 'items' collection already exists, skipping data insertion.")


# --- API Routes (same as before, for demonstration) ---

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/items', methods=['GET'])
def get_items():
    try:
        items = list(mongo.db.items.find())
        return jsonify(items)
    except Exception as e:
        return jsonify({'message': 'Error getting items', 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
