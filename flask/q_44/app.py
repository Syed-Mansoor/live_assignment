# Creating a RESTful API Endpoint in Flask that Returns JSON Data
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'syed mansoor',
        'age': 23,
        'city': 'jammu and kashmir'
    }
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)