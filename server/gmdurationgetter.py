#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time
import datetime

class GMDurationGetter:
    def get_duration(self, origin = "Brooklyn", destination = "Queens", departure_time = datetime.datetime.now()):
        url = 'http://maps.googleapis.com/maps/api/directions/json'

        params = dict(
            mode='transit',
            origin=origin,
            destination=destination,
            departure_time=departure_time.strftime('%s')
        )

        return self.query_google_maps(url, params)

    def query_google_maps(self, url, params):
        attempts = 0
        success = False
        while success != True and attempts < 4:
            resp = requests.get(url=url, params=params)
            attempts += 1
            data = json.loads(resp.text)
            status = data["status"]
            if status == "OVER_QUERY_LIMIT":
                time.sleep(2)
                # retry
                continue
            success = True

        if attempts == 4:
            print "Daily limit has been reached"
            return -1

        if success:
            route = data["routes"][0]
            legs = route["legs"][0]
            duration = legs["duration"]
            return duration["value"]

if __name__ == '__main__':
    gm_duration_getter = GMDurationGetter()
    print gm_duration_getter.get_duration("Fyrisgrand 13, Bagarmossen", "Sveavagen 42, Stockholm", datetime.datetime(2016, 8, 1, 8, 0));