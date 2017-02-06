#TESTING
import os.path
from flask import Flask, send_file, send_from_directory, jsonify
import booligetter
import gmdurationgetter
import datetime

BASE_URL = os.path.abspath(os.path.dirname(__file__))
#print BASE_URL
CLIENT_APP_FOLDER = os.path.abspath(os.path.join(BASE_URL, "../client/dist/"))
#print CLIENT_APP_FOLDER
APP_FOLDER = os.path.abspath(os.path.join(BASE_URL, "../client/dist/app"))
#print APP_FOLDER

class Komute2Server:
    def __init__(self, duration_getter, listings_getter):
        self.app = Flask(__name__, static_url_path='')
        self.duration_getter = duration_getter
        self.listings_getter = listings_getter
        self.add_routes()

    def add_routes(self):
        @self.app.route('/')
        def hello_world(self):
             return send_from_directory(CLIENT_APP_FOLDER, 'index.html')

        @self.app.route('/client/<path:path>')
        def send_client(path):
            return send_from_directory(CLIENT_APP_FOLDER, path)

        @self.app.route('/app/<path:path>')
        def send_app(path):
            return send_from_directory(APP_FOLDER, path)

        @self.app.route('/api/listings', methods = ['GET'])
        def get_listings():
           listings = booligetter.QueryBooli();
           return jsonify({'listings': listings})

        @self.app.route('/api/duration', methods = ['GET'])
        def get_duration(self):
           duration = self.booliGetter.GetDuration("Fyrisgrand 13, Bagarmossen", "Sveavagen 42, Stockholm", datetime.datetime(2016,8,1,8,0));
           return jsonify({'duration': duration})

    def start_server(self):
        self.app.run()

if __name__ == "__main__":
    restfulServer = Komute2Server(gmdurationgetter, booligetter)
    restfulServer.start_server()