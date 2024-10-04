from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Appliquer CORS à toute l'application
    CORS(app)  # Permet toutes les origines. Vous pouvez restreindre à une origine spécifique si nécessaire.
    
    from .routes import main
    app.register_blueprint(main)

    return app
