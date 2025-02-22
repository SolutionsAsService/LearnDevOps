from flask import Flask, request, jsonify
import jwt  # Used for creating JWT tokens
import datetime  # Handles expiration times
import bcrypt  # Secure password hashing
import os  # Access environment variables

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret')  # Secret key for JWT signing

# Simulated user database (in-memory for example purposes)
users = {
    "user": bcrypt.hashpw("pass".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
}

@app.route('/api/auth/login', methods=['POST'])
def login():
    """Handles user authentication and returns a JWT token if valid."""
    data = request.get_json()
    username, password = data.get('username'), data.get('password')

    if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username].encode('utf-8')):
        token = jwt.encode({
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({"token": token}), 200

    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
