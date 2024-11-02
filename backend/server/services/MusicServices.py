from datetime import datetime
from flask import jsonify
import pymongo
import pickle
from bson.binary import Binary
import ENV as ENV
import base64
from bson import ObjectId

from ..utils.DatabaseUtils import *

def fetchAllMusic():
    music_collection = loadMusics()
    musics = music_collection.find({})
    music_list = []
    
    for music in musics:
        music['_id'] = str(music['_id'])
        if 'audio' in music:
            music['audio'] = base64.b64encode(music['audio']).decode('utf-8')
        music_list.append(music)
    return music_list

def insertMusic(data):
    music_collection = loadMusics()
    required_fields = ["title", "audio"]
    for field in required_fields:
        if field not in data:
            print(f"Error: '{field}' is missing from input data.")
            return f"error: missing field '{field}'"

    try:    
        new_music_document = {
            "title": data["title"],
            "album": data["album"],
            "author": data["author"],
            "date_added": datetime.now(), 
            "alike":[],        
            "audio": Binary(data["audio"]) if isinstance(data["audio"], bytes) else None
        }
    except Exception as e:
        print("Error creating document:", e)
        return "error creating document"    
    
    try:
        result = music_collection.insert_one(new_music_document)
    except Exception as e:
        print("Error inserting music:", e)
        return "error inserting music"

    print("Insertion result: {result.inserted_id}")
    return str(result.inserted_id)

