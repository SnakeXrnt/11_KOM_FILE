from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] =
app.config['SQLALCHEMY_DATABASE_URI'] =
app.config['SQLALCHEMY_DATABASE_URI'] =
db = SQLAlchemy(app)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)