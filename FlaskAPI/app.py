# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import datetime;

from sheets import addPhoto

# creating a Flask app
app = Flask(__name__)
CORS(app)
# app.secret_key = b'_53oi3uriq9pifpff;apl'
# csrf = CSRFProtect(app)

@app.route('/api', methods = ['GET', 'POST'])
@cross_origin()
def home():
    if request.method == 'POST':
        body = request.get_json()
        print('Request recieved')
        # Process it
        addPhoto(body['timestamp'], body['screenshotUrl'])

        response = jsonify({'you sent': body})
        return response


# driver function
if __name__ == '__main__':

	app.run(debug = True)
