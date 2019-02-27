from flask import render_template 
from flask import request 
from app import app

@app.route('/', methods=['GET'])
def index():
    return "testing"
