#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time
import datetime
from random import randint

def GetDuration(origin, destination, departure_time = datetime.datetime.now()):
    # gkey = "AIzaSyA5wyYzwUiBwIFCKrSxWlWLP7VSrvzUvG0"
    return randint(100,1000)

    url = 'http://maps.googleapis.com/maps/api/directions/json'
    #http://maps.googleapis.com/maps/api/directions/json?origin=Brooklyn&destination=Queens&key=API_KEY&departure_time=1343641500&mode=transit

    params = dict(
        mode='transit',
        origin=origin,
        destination=destination,
        departure_time=departure_time.strftime('%s')
        # key=gkey
    )

    attempts = 0
    success = False

    while success != True and attempts < 4:
        resp = requests.get(url=url, params=params)
        attempts += 1
        # The GetStatus function parses the answer and returns the status code
        data = json.loads(resp.text)
        status = data["status"]
        print status
        if status == "OVER_QUERY_LIMIT":
            time.sleep(2)
            # retry
            continue
        success = True

    if attempts == 4:
          # send an alert as this means that the daily limit has been reached
          print "Daily limit has been reached"

    if success:
        # print data
        route = data["routes"][0]
        legs = route["legs"][0]
        duration = legs["duration"]
        return duration["value"]

if __name__ == '__main__':
    print GetDuration("Fyrisgrand 13, Bagarmossen", "Sveavagen 42, Stockholm", datetime.datetime(2016,8,1,8,0));