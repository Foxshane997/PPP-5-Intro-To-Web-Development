from flask import Flask

def create_app():
    app = Flask(__name__)

# Index Route with a hello function
    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    return app