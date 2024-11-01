from flask import Flask
from flask import Flask
from flask_cors import CORS
from server.MusicServer import musicBlueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(musicBlueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
