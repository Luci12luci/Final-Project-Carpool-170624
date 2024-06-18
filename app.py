from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://u1ai5zsuzpe6y74uwyqu:0BacMZwIRVg5rpsOcndFG1pcHSUba5@by1wvfyyi5kgu1euhyko-postgresql.services.clever-cloud.com:50013/by1wvfyyi5kgu1euhyko"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)

users = {
    'john': 'password123',
    'jane': 'mypassword'
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('welcome', username=username))
        else:
            error = "Invalid username or password"
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
