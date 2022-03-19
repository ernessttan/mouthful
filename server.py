from turtle import update
from venv import create
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


# Home Page Route #
@app.route('/')
def home():
    return render_template('layout.html')

if __name__ == '__main__':
   app.run(debug = True)