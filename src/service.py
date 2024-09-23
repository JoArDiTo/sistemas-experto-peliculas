from flask import Blueprint, request, jsonify
from .function import inference_engine

recommends = Blueprint('recommends', __name__)

@recommends.route('/recommend', methods=['POST'])
def get_recommendations():
    params = request.json
    recommendations = inference_engine(params)
    
    if recommendations:
        return jsonify(recommendations)
    else:
        return jsonify({"message": "No se encontraron películas que coincidan con los criterios."})