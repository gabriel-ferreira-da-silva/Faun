

from flask import Blueprint, json, jsonify, request
from utils.DatabaseUtils import *

musicBlueprint = Blueprint('music_blueprint', __name__)

@musicBlueprint.route("/music", methods=['GET'])
def get_music():
    try:
        musics = fetchAllMusic()
        return jsonify(musics)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500