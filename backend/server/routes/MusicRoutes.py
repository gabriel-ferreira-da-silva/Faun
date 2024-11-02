from flask import Blueprint, json, jsonify, request
from ..utils.MusicUtils import *
from ..services.MusicServices import *

musicBlueprint = Blueprint('music_blueprint', __name__)

@musicBlueprint.route("/music", methods=['GET'])
def get_music():
    try:
        musics = fetchAllMusic()
        return jsonify(musics)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@musicBlueprint.route("/music/add", methods=['POST'])
def insert_new_model():
    try:
        
        data = {
            "title": request.form.get("title"),
            "album": request.form.get("album"),
            "author": request.form.get("author"),
        }

        
        file = request.files.get("audio")
        if file:
            data["audio"] = Binary(file.read())
        else:
            return jsonify({"error": "Model file is missing"}), 400

        
        result = insertMusic(data)
        print(result)

        return jsonify({"result": result}), 201
    except Exception as e:
        print("Error adding music:", e)
        return jsonify({"error": "Failed to add new model"}), 500
    