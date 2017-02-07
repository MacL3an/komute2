from booligetter import BooliGetter
import json

class DummyBooliGetter(BooliGetter):
    def get_listings(self, url):
        return self.dummy_listing_data()

    def dummy_listing_data(self, *args):
        test = json.loads("""[
            {
              "booliId": 2253361,
              "constructionYear": 1929,
              "floor": 3,
              "listPrice": 3475000,
              "livingArea": 52,
              "location": {
                "address": {
                  "streetAddress": "Thorildsv\u00e4gen 5"
                },
                "namedAreas": [
                  "Kungsholmen"
                ],
                "position": {
                  "latitude": 59.33227009,
                  "longitude": 18.01635504
                },
                "region": {
                  "countyName": "Stockholms l\u00e4n",
                  "municipalityName": "Stockholm"
                }
              },
              "objectType": "L\u00e4genhet",
              "plotArea": 0,
              "published": "2017-02-03 23:52:12",
              "rent": 3039,
              "rooms": 2,
              "source": {
                "id": 1564,
                "name": "Erik Olsson Fastighetsf\u00f6rmedling",
                "type": "Broker",
                "url": "http://www.erikolsson.se/"
              },
              "url": "https://www.booli.se/annons/2253361"
            },
            {
              "booliId": 2177621,
              "constructionYear": 2016,
              "floor": 5,
              "listPrice": 3975000,
              "livingArea": 53,
              "location": {
                "address": {
                  "streetAddress": "Hornsbergs Strand 15C"
                },
                "namedAreas": [
                  "Kungsholmen"
                ],
                "position": {
                  "latitude": 59.34049523,
                  "longitude": 18.00779643
                },
                "region": {
                  "countyName": "Stockholms l\u00e4n",
                  "municipalityName": "Stockholm"
                }
              },
              "objectType": "L\u00e4genhet",
              "published": "2017-02-03 22:11:11",
              "rent": 2871,
              "rooms": 2,
              "source": {
                "id": 410,
                "name": "Edward & Partners Fastighetsm\u00e4klare AB",
                "type": "Broker",
                "url": "http://www.edwardpartners.se/"
              },
              "url": "https://www.booli.se/annons/2177621"
            }
          ]""")
        return test