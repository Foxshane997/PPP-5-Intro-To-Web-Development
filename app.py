# Config
from flask import Flask
app = Flask(__name__)


# Index Route
@app.route('/')
def index():
    return 'Hello, this is a PetFax!'

# Pets Index route
@app.route('/pets')
def pets():
    return 'These are our pets available for adoption!'