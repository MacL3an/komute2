import time
from hashlib import sha1
import random
import string
import requests
import urlparse
import re
import json

def GetData(args):
    callerId = "MacL3an"
    timestamp = str(int(time.time()))
    unique = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(16))
    hashstr = sha1(callerId+timestamp+"LWfD8NBtmLVFnusBZURfhgABvnu3JpvhslQEWNvR"+unique).hexdigest()

    #url = "/listings?q="+area+"&callerId="+callerId+"&time="+timestamp+"&unique="+unique+"&hash="+hashstr

    url = 'http://api.booli.se/listings'
    args["hash"] = hashstr
    args["time"] = timestamp
    args["unique"]=unique
    args["callerId"]=callerId

    response = requests.get(url=url, params=args)

    if response.status_code != 200:
        raise Exception("failed getting data from Booli")

    return response.text
#    f = open('boolidata.txt', 'w')
#    f.write(data)
#    f.close

def QueryBooli():
    url = "http://www.booli.se/kristineberg/874669/?objectType=l%C3%A4genhet&rooms=2"
    areaIds = re.sub('^booli.*\n', '', url)
    parsedurl = urlparse.urlparse(url)
    areas = parsedurl.path.split('/')
    areaNames = areas[1]
    areaIds = areas[2]
    args = urlparse.parse_qs(parsedurl.query)
    args['areaId'] = areaIds

    #filename = 'boolidata.txt'
    #f = open(filename)
    #data = json.load(f)

    boolidata = GetData(args)
    data = json.loads(boolidata)
    listings = data["listings"]
    print listings
    return listings

if __name__ == '__main__':
    print GetData();