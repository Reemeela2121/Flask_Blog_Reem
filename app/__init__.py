import os
from dotenv import load_dotenv
from . import db

from app.db import get_db

from flask import Flask, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

@app.route('/')
def index():
    index_list = ["We are", "R2T2", "MLH Orientation Week Hackathon Submission", "description here"]
    return render_template('index.html', title=index_list[0], title2=index_list[1], page_header=index_list[1], top_page_title=index_list[2], desc=index_list[3], url=os.getenv("URL"))

@app.route('/team_profiles')
def team_profiles():
    return render_template('team_profiles.html', page_header="Meet the team", top_page_title="MLH Orientation Week Hackathon Submission")

@app.route('/temp')
def temp():
    return render_template('temp.html')


@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f"User {username} is already registered."

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return f"User {username} created successfully"
        else:
            return error, 418

    ## TODO: Return a register page
    return "Register Page not yet implemented", 501


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            return "Login Successful", 200 
        else:
            return error, 418
    
    ## TODO: Return a login page
    return "Login Page not yet implemented", 501