from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/boom')
def boom():
    return 'duar!'

# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 