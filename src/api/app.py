from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the City AI Engine!"})

@app.route('/api/data')
def get_data():
    # Sample data
    data = {"city": "ExampleCity", "population": 500000}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
