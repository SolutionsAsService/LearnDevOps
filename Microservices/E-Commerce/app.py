# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple endpoint for user authentication
@app.route('/api/users/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # (Here you would normally verify credentials)
    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful", "token": "abcdef12345"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
