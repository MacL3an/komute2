from flask import Flask, request, jsonify, send_file
from booligetter import BooliGetter
from dummybooligetter import DummyBooliGetter
from gmdurationgetter import GMDurationGetter
from dummydurationgetter import DummyDurationGetter
import datetime
import urllib

class Komute2Server:
    def __init__(self, listings_getter, duration_getter):
        self.app = Flask(__name__)
        self.duration_getter = duration_getter
        self.listings_getter = listings_getter
        self.add_routes()

    def add_routes(self):
        @self.app.route("/")
        def index():
            return send_file("templates/index.html")

        @self.app.route('/api/listings', methods = ['GET'])
        def get_listings():
            booliurl = urllib.unquote(request.query_string)
            listings = self.listings_getter.get_listings(booliurl);
            return jsonify({'listings': listings})

        @self.app.route('/api/duration', methods = ['GET'])
        def get_duration():
            origin = request.args.get('origin')
            destination = request.args.get('destination')
            transitType = request.args.get('transitType')
            duration = self.duration_getter.get_duration(origin, destination, transitType);
            return jsonify({'duration': duration})

    def start_server(self):
        self.app.run(host='0.0.0.0')

if __name__ == "__main__":
    booli_getter = BooliGetter()
    duration_getter = GMDurationGetter()
    # booli_getter = DummyBooliGetter()
    # duration_getter = DummyDurationGetter()
    restfulServer = Komute2Server(booli_getter, duration_getter)
    restfulServer.start_server()