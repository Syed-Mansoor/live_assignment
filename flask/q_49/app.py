# import os
# from flask import Flask, render_template, request, redirect, url_for, session
# from flask_bcrypt import Bcrypt
# from pymongo import MongoClient

# app = Flask(__name__)
# app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')
# bcrypt = Bcrypt(app)

# # Configure MongoDB
# MONGO_URI = "mongodb+srv://saeedmansoor56:<d8qt%F.R?uJiffb>@cluster0.l7pvtux.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# client = MongoClient(MONGO_URI)
# db = client['flask_mongo_app']
# users = db['users']

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
#         users.insert_one({'username': username, 'password': hashed_pw})
#         return redirect(url_for('login'))
#     return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == ['POST']:
#         username = request.form['username']
#         password = request.form['password']
#         user = users.find_one({'username': username})
#         if user and bcrypt.check_password_hash(user['password'], password):
#             session['username'] = username
#             return redirect(url_for('dashboard'))
#     return render_template('login.html')

# @app.route('/dashboard')
# def dashboard():
#     if 'username' in session:
#         return render_template('dashboard.html', username=session['username'])
#     return redirect(url_for('login'))

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)


import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from urllib.parse import quote_plus

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')
bcrypt = Bcrypt(app)

# Configure MongoDB
username = quote_plus("saeedmansoor56")
password = quote_plus("<d8qt%F.R?uJiffb>")
MONGO_URI = f"mongodb+srv://{username}:{password}@cluster0.l7pvtux.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client['flask_mongo_app']
users = db['users']

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        users.insert_one({'username': username, 'password': hashed_pw})
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.find_one({'username': username})
        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
