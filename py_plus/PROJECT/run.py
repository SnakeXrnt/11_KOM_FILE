from pickle import FALSE
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = FALSE
db = SQLAlchemy(app)

class Item(db.Model):\
	id = db.Column(db.Integer, primary_key=True , autoincrement=True)
	status = db.Column(db.Boolean, nullable=False,default=True)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)