from flask import Flask, jsonify, request
# from flask_restful import Resource, Api 
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/boom')
def hello_world():
    return 'duar!'

