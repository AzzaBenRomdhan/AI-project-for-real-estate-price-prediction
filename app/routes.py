from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from .model.model import make_prediction

main = Blueprint('main', __name__)

@main.route('/predict', methods=['POST', 'OPTIONS'])
@cross_origin()
def predict():
    try:
        data = request.json

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Assurez-vous que les données sont bien au format attendu
        if not all(key in data for key in ['lotSize', 'bedrooms', 'bathrooms', 'garageSize', 'yearOfBuild']):
            return jsonify({'error': 'Missing fields in data'}), 400

        # Faites la prédiction
        prediction = make_prediction(data)
        return jsonify({'prediction': prediction}), 200

    except Exception as e:
        # Log de l'erreur et retour d'une réponse d'erreur appropriée
        print(f"Erreur lors de la prédiction: {str(e)}")
        return jsonify({'error': str(e)}), 500
