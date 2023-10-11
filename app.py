from flask import Flask, jsonify
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
    webbrowser.open("http://localhost:5000//user/" + fetch_uid()) 
    app.run(debug=True)
