import time
from hashlib import sha1
import random
import string
import requests
import urlparse
import re
import json

class BooliGetter:
    def __init__(self, callerId = "MacL3an", key = "LWfD8NBtmLVFnusBZURfhgABvnu3JpvhslQEWNvR"):
        self.callerId = callerId
        self.key = key

    def perform_query(self, args):
        timestamp = str(int(time.time()))
        unique = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(16))
        hashstr = sha1(self.callerId + timestamp + self.key + unique).hexdigest()

        #url = "/listings?q="+area+"&callerId="+callerId+"&time="+timestamp+"&unique="+unique+"&hash="+hashstr

        url = 'http://api.booli.se/listings'
        args["hash"] = hashstr
        args["time"] = timestamp
        args["unique"]=unique
        args["callerId"]=self.callerId

        response = requests.get(url=url, params=args)

        if response.status_code != 200:
            raise Exception("failed getting data from Booli")

        return response.text

    def parse_url(self, url):
        parsedurl = urlparse.urlparse(url)
        areas = parsedurl.path.split('/')
        areaIds = areas[2]
        args = urlparse.parse_qs(parsedurl.query)
        args['areaId'] = areaIds
        return args

    def get_listings(self, url = "http://www.booli.se/kristineberg/874669/?objectType=l%C3%A4genhet&rooms=2"):
        args = self.parse_url(url)

        result = self.perform_query(args)
        data = json.loads(result)
        listings = data["listings"]
        return listings

if __name__ == '__main__':
    booliGetter = BooliGetter()
    print booliGetter.get_listings()