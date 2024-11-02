#!/usr/bin/env python3

import pymongo
from bson.binary import Binary
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['faun_database']
music_collection = db['music']

with open("Like A Tattoo.mp3", 'rb') as f:
    like_a_tattoo = f.read()

like_a_tattoo_mp3 = {
    "title": "like a tattoo",
    "author": "sade",
    "album": "love deluxe",
    "date_added": datetime.now(),
    "alike":[],
    "audio": Binary(like_a_tattoo),
}

result = music_collection.insert_one( like_a_tattoo_mp3)
print(f"Model inserted with _id: {result.inserted_id}")
