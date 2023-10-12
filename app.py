from flask import Flask, jsonify, request
import webbrowser

app = Flask(__name__)

# Mock user data
users = {
    '123456': {
        'uid': '123456',
        'name': 'John Doe',
        'password': 'hashed_password_here',  # This should be hashed in a real scenario
        'email': 'john.doe@example.com',
        'fitbit_data': 'Sample Fitbit data'
    }
}

@app.route('/')
def index():
    return "Welcome to the Health Data Management App!"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # Get data from the request
    
    # Check if user already exists
    if data['uid'] in users:
        return jsonify({'message': 'User already exists'}), 400
    
    # In reality, ensure you're hashing the password
    users[data['uid']] = {
        'uid': data['uid'],
        'name': data['name'],
        'password': data['password'],
        'email': data['email'],
        'fitbit_data': ""  # No fitbit data at registration
    }
    
    return jsonify({'message': 'Registered successfully'}), 201

@app.route('/user/<uid>', methods=['GET'])
def get_user(uid):
    user = users.get(uid)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404
    
def fetch_uid():
    return "123456"


if __name__ == '__main__':
    webbrowser.open("http://localhost:5000/user/" + fetch_uid()) 
    app.run(debug=True)
