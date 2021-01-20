"""Cloud Foundry test"""
from flask import Flask, request, render_template, jsonify
import os
import psycopg2
import csv
import json

port = 5432

app = Flask(__name__)

wport = int(os.getenv("PORT"))

# 2020.12.18
@app.route('/')
def hello_world():
    return 'Hello World! I am running on port ' + str(wport)




# 2020.12.11
if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=wport)
