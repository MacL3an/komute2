#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time
import datetime

class GMDurationGetter:
    def get_duration(self, origin = "Brooklyn", destination = "Queens", mode='transit', departure_time = None):
        url = 'http://maps.googleapis.com/maps/api/directions/json'

        if departure_time is None:
            departure_time = self.get_next_monday_morning()
            print departure_time

        params = dict(
            mode=mode,
            origin=origin,
            destination=destination,
            departure_time=departure_time.strftime('%s')
        )

        return self.query_google_maps(url, params)

    def get_next_monday_morning(self):
        d = datetime.date.today()
        while (d.weekday() != 0):
            d += datetime.timedelta(1)

        return datetime.datetime(d.year, d.month, d.day, 8, 0)

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
    print gm_duration_getter.get_duration("Fyrisgrand 13, Bagarmossen", "Sveavagen 42, Stockholm", datetime.datetime(2017, 2, 20, 8, 0));