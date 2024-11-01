

from flask import Blueprint, json, jsonify, request

musicBlueprint = Blueprint('diseases_blueprint', __name__)

@musicBlueprint.route("/music", methods=['GET'])
def get_diseases():
    try:
        return jsonify({"title":"hello", "author":"world"})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500