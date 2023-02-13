import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/dlr', methods=['POST'])
def dlr():
    message = request.form['message']
    sender = request.form['sender']
    # Forward the incoming message to the API
    response = requests.post('https://check.properseals.org/api/v1/properseals/verify/product/serial_number/', json={'message': message, 'sender': sender})
    # Extract the result from the API response
    result = response.json()['result']
    # Send the result back to Kannel
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
