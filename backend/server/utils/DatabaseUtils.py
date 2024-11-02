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

