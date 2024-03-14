# import the library
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import secrets, hashlib, os
import logging
from functools import wraps

app = Flask(__name__)

# database configuration (the uri need to be change base on the user environment)
# using alibaba could to be the mysql server
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Tan011205@rm-bp110at41skc47s4nzo.mysql.rds.aliyuncs.com/dashmote_case'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 

# Log configuration 
# (specifying log file path and logging level)
log_folder = os.getcwd()  # need to be change based on the user environment
log_file = os.path.join(log_folder, 'app.log') 
if not os.path.exists(log_folder):
    os.makedirs(log_folder)  
logging.basicConfig(filename=log_file, level=logging.DEBUG)

# Token configuration, generating and saving or reading application keys
token_folder = os.getcwd()  # need to be change based on the user environment
token_file_path = os.path.join(token_folder, 'token.txt')  
# If the token folder does not exist, create
if not os.path.exists(token_folder):
    os.makedirs(token_folder)  
# if the token folder exist
if not os.path.isfile(token_file_path):
    # write the new token
    app.config['SECRET_KEY'] = secrets.token_hex(16) 
    with open(token_file_path, "w") as token_file: 
        token_file.write(app.config['SECRET_KEY'])
else:
    # read the token
    with open(token_file_path, "r") as token_file: 
        app.config['SECRET_KEY'] = token_file.read().strip()

# Authentication decorator
# used to protect routing and ensure access is only allowed when the correct token is provided
def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization') 
        # If the token is invalid, return 401 Unauthorized
        if not token or token != app.config['SECRET_KEY']:
            return jsonify({'message': 'Unauthorized'}), 401 
        return f(*args, **kwargs)
    return decorated_function

# Defining Restaurant Data Models
class Restaurant(db.Model):
    __tablename__ = 'restaurants'  # table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    cuisine = db.Column(db.String(128), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    contact_phone = db.Column(db.String(64), nullable=False)
    contact_email = db.Column(db.String(128), nullable=False)

    # hash for encryption
    @staticmethod
    def hash_string(string_to_hash):
        return hashlib.sha256(string_to_hash.encode()).hexdigest()

# Define routing for processing restaurant information
@app.route('/restaurants', methods=['GET', 'POST'])
@auth_required  
def restaurants():
    # GET request and return restaurant list
    if request.method == 'GET':
        # get the page number, if not then set the page = 1
        page = request.args.get('page', 1, type=int) 
        per_page = request.args.get('per_page', 10, type=int)  
        # get the location and cuisine type
        location = request.args.get('location') 
        cuisine = request.args.get('cuisine') 

        # query the restaurant and filter by location and cuisine
        query = Restaurant.query  
        if location:
            query = query.filter(Restaurant.location.ilike(f'%{location}%'))  
        if cuisine:
            query = query.filter(Restaurant.cuisine.ilike(f'%{cuisine}%'))  

        # exeute the pagination
        paginated_restaurants = query.paginate(page=page, per_page=per_page, error_out=False)
        restaurants = paginated_restaurants.items  

        return jsonify({
            'restaurants': [
                {'id': r.id, 'name': r.name, 'location': r.location, 'cuisine': r.cuisine, 'rating': r.rating,
                 'contact': {'phone': r.contact_phone, 'email': r.contact_email}}
                for r in restaurants
            ],
            'total': paginated_restaurants.total,
            'pages': paginated_restaurants.pages,
            'current_page': page
        }), 200
    # POST requests and add new restaurants
    elif request.method == 'POST':
        data = request.json
        new_restaurant = Restaurant(
            name=data['name'],
            location=data['location'],
            cuisine=data['cuisine'],
            rating=data['rating'],
            contact_phone=data['contact']['phone'],
            contact_email=data['contact']['email']
        )
        db.session.add(new_restaurant)
        db.session.commit() 
        return jsonify({'message': 'Restaurant added successfully', 'id': new_restaurant.id}), 201

# Define routing for processing individual restaurant information
@app.route('/restaurants/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@auth_required  
def restaurant_operations(id):
    #Query restaurant by ID, if not found, return 404
    restaurant = Restaurant.query.get_or_404(id)  
    if request.method == 'GET':
        return jsonify({
            'id': restaurant.id,
            'name': restaurant.name,
            'location': restaurant.location,
            'cuisine': restaurant.cuisine,
            'rating': restaurant.rating,
            'contact': {'phone': restaurant.contact_phone, 'email': restaurant.contact_email}
        }), 200
    #Update restaurant information
    elif request.method == 'PUT':
        data = request.json
        restaurant.name = data.get('name', restaurant.name)
        restaurant.location = data.get('location', restaurant.location)
        restaurant.cuisine = data.get('cuisine', restaurant.cuisine)
        restaurant.rating = data.get('rating', restaurant.rating)
        restaurant.contact_phone = data['contact']['phone']
        restaurant.contact_email = data['contact']['email']
        db.session.commit()  
        return jsonify({'message': 'Restaurant updated successfully'}), 200
    #Delete Restaurant
    elif request.method == 'DELETE':
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify({'message': 'Restaurant deleted successfully'}), 200

# start with application
if __name__ == '__main__':
    app.run(debug=True)
