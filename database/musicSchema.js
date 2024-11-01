use('FaunDatabase')

db.createCollection("music", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required:["title", "audio"],
      properties: {
        title: {
            bsonType: "string",
            description: "music title"
        },
        author: {
            bsonType: "string",
            description: "music author"
        },
        album: {
            bsonType: "string",
            description: "album of the music"
        },
        date_added: {
          bsonType: ["date", "null"],
          description: "date added to faun database"
        },
        alike: {
            bsonType: ["string"],
            description: "date added to faun database"
        },
        audio: {
          bsonType: "binData",
          description: "The actual machine learning model serialized as binary data"
        }
      }
    }
  }
})

db.music.createIndex({ title: 1 }, { unique: true });