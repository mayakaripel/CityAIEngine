from flask import Flask, jsonify
from flask_restx import Api, Resource, fields
from marshmallow import Schema, fields as ma_fields, ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

# --- Initialize App and Extensions ---
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///city_data.db'  # Example using SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret'  # Change this to a random secret
api = Api(app, version='1.0', title='City AI Engine API', 
          description='API for accessing city data', doc='/docs')

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize JWT
jwt = JWTManager(app)

# --- Database Model ---
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    area = db.Column(db.String(50), nullable=False)

# --- Data Model and Validation ---
class CityDataSchema(Schema):
    city = ma_fields.Str(required=True)
    population = ma_fields.Int(required=True)
    area = ma_fields.Str(required=True)

city_schema = CityDataSchema()

# --- API Resource ---
@api.route('/api/v1/data')
class CityData(Resource):
    @jwt_required()  # Protect this endpoint with JWT authentication
    def get(self):
        """
        Get data for a sample city.
        """
        # In a real application, you would fetch data from a database here.
        cities = City.query.all()
        data = [{"city": city.city, "population": city.population, "area": city.area} for city in cities]

        return jsonify(data)

    def post(self):
        """
        Create a new city entry.
        """
        try:
            data = city_schema.load(api.payload)
            new_city = City(**data)
            db.session.add(new_city)
            db.session.commit()
            return city_schema.dump(new_city), 201
        except ValidationError as err:
            return jsonify(err.messages), 400  # Return validation errors
        except Exception as e:
            return jsonify({"error": str(e)}), 500  # Handle generic errors

# --- User Authentication ---
@api.route('/api/v1/login')
class UserLogin(Resource):
    def post(self):
        username = api.payload.get('username')
        password = api.payload.get('password')
        # Here you would normally verify the username and password
        # For demonstration purposes, we’ll skip the actual authentication logic.
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

if __name__ == '__main__':
    # Create the database if it doesn't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
