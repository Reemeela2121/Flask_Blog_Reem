import os
from sqlite3 import dbapi2
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv
from flask.helpers import url_for

load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
dbapi2.init_app(app)

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
