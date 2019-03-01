from flask import render_template 
from flask import request 
from app import app
from app import process_data

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", data=process_data.process())
