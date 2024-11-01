from datetime import datetime
from flask import jsonify
import pymongo
import pickle
from bson.binary import Binary
import ENV as ENV

import base64

from bson import ObjectId


def loadMusics():
    client = pymongo.MongoClient(ENV.DATABASE_URL, serverSelectionTimeoutMS=5000) 
    db = client[ENV.DATABASE_NAME]
    models_collection = db['music']
    return models_collection


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


