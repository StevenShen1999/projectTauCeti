from flask import Flask, request, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# TODO: Add whatever