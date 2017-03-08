from booligetter import BooliGetter
import json

class DummyBooliGetter(BooliGetter):
    def get_listings(self, url):
        return self.dummy_listing_data()

    def dummy_listing_data_short(self, *args):
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
            },
            {
              "booliId": 1234,
              "constructionYear": 2016,
              "floor": 5,
              "listPrice": 5000000,
              "livingArea": 100,
              "location": {
                "address": {
                  "streetAddress": "Testgata 1"
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
              "rooms": 3,
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

    def dummy_listing_data(self, *args):
        test = json.loads("""[
      {
        "additionalArea": 15,
        "booliId": 2272819,
        "constructionYear": 1973,
        "listPrice": 3825000,
        "livingArea": 124,
        "location": {
          "address": {
            "streetAddress": "\u00d6rnholmsbrinken 140"
          },
          "namedAreas": [
            "V\u00e5rberg"
          ],
          "position": {
            "latitude": 59.27291186,
            "longitude": 17.87409655
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Radhus",
        "plotArea": 214,
        "published": "2017-03-04 11:25:35",
        "rooms": 5,
        "source": {
          "id": 1598,
          "name": "M\u00e4klarringen",
          "type": "Broker",
          "url": "http://www.maklarringen.se/"
        },
        "url": "https://www.booli.se/annons/2272819"
      },
      {
        "additionalArea": 24,
        "booliId": 2271050,
        "constructionYear": 1968,
        "listPrice": 3395000,
        "livingArea": 126,
        "location": {
          "address": {
            "streetAddress": "Tankebyggarbacken 85"
          },
          "namedAreas": [
            "Sk\u00e4rholmen"
          ],
          "position": {
            "latitude": 59.29250264,
            "longitude": 17.92765203
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Radhus",
        "plotArea": 213,
        "published": "2017-03-02 17:16:08",
        "rooms": 5,
        "source": {
          "id": 1561,
          "name": "Bjurfors",
          "type": "Broker",
          "url": "http://www.bjurfors.se/"
        },
        "url": "https://www.booli.se/annons/2271050"
      },
      {
        "additionalArea": 52,
        "booliId": 2155577,
        "constructionYear": 1964,
        "listPrice": 5675000,
        "livingArea": 105,
        "location": {
          "address": {
            "streetAddress": "Sk\u00f6nstaviks All\u00e9 26"
          },
          "namedAreas": [
            "Sk\u00f6ndal"
          ],
          "position": {
            "latitude": 59.25013651,
            "longitude": 18.11555309
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Radhus",
        "plotArea": 137,
        "published": "2017-03-02 16:34:01",
        "rooms": 6,
        "source": {
          "id": 1610,
          "name": "HusmanHagberg",
          "type": "Broker",
          "url": "http://www.husmanhagberg.se/"
        },
        "url": "https://www.booli.se/annons/2155577"
      },
      {
        "additionalArea": 53,
        "booliId": 2267067,
        "constructionYear": 1952,
        "listPrice": 5950000,
        "livingArea": 120,
        "location": {
          "address": {
            "streetAddress": "Vivstavarvsv\u00e4gen 191"
          },
          "namedAreas": [
            "Enskede"
          ],
          "position": {
            "latitude": 59.28255463,
            "longitude": 18.0496273
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Radhus",
        "plotArea": 306,
        "published": "2017-02-28 16:25:03",
        "rooms": 6,
        "source": {
          "id": 204,
          "name": "M\u00e4klarhuset",
          "type": "Broker",
          "url": "http://www.maklarhuset.se/"
        },
        "url": "https://www.booli.se/annons/2267067"
      },
      {
        "booliId": 2266673,
        "constructionYear": 2017,
        "listPrice": 6650000,
        "livingArea": 140,
        "location": {
          "address": {
            "streetAddress": "Fanny Brates v\u00e4g 4"
          },
          "namedAreas": [
            "Sk\u00f6ndal"
          ],
          "position": {
            "latitude": 59.25859833,
            "longitude": 18.12777519
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2017-02-27 19:15:16",
        "rent": 4940,
        "rooms": 6,
        "source": {
          "id": 204,
          "name": "M\u00e4klarhuset",
          "type": "Broker",
          "url": "http://www.maklarhuset.se/"
        },
        "url": "https://www.booli.se/annons/2266673"
      },
      {
        "booliId": 2266282,
        "listPrice": 11000000,
        "livingArea": 159,
        "location": {
          "address": {
            "streetAddress": "Thunbergsgatan"
          },
          "namedAreas": [
            "Hammarbyh\u00f6jden"
          ],
          "position": {
            "latitude": 59.29564044,
            "longitude": 18.09615612
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Radhus",
        "plotArea": 160,
        "published": "2017-02-27 03:55:26",
        "rooms": 5,
        "source": {
          "id": 58,
          "name": "Svenska M\u00e4klarhuset",
          "type": "Broker",
          "url": "http://www.svenskamaklarhuset.se/"
        },
        "url": "https://www.booli.se/annons/2266282"
      },
      {
        "additionalArea": 79,
        "booliId": 2265003,
        "listPrice": 5250000,
        "livingArea": 80,
        "location": {
          "address": {
            "streetAddress": "J\u00e4rflottav\u00e4gen 12"
          },
          "namedAreas": [
            "\u00d6rby"
          ],
          "position": {
            "latitude": 59.26656729,
            "longitude": 18.02557589
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "plotArea": 668,
        "published": "2017-02-24 13:12:43",
        "rooms": 6,
        "source": {
          "id": 1601,
          "name": "S\u00f6derm\u00e4klarna",
          "type": "Broker",
          "url": "http://www.sodermaklarna.se/"
        },
        "url": "https://www.booli.se/annons/2265003"
      },
      {
        "booliId": 2264953,
        "constructionYear": 2006,
        "listPrice": 5650000,
        "livingArea": 128,
        "location": {
          "address": {
            "streetAddress": "Sylvestergatan 6B"
          },
          "namedAreas": [
            "\u00c4lvsj\u00f6"
          ],
          "position": {
            "latitude": 59.28499,
            "longitude": 18.03127
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Radhus",
        "published": "2017-02-24 12:53:11",
        "rent": 6195,
        "rooms": 5,
        "source": {
          "id": 713,
          "name": "Svensk Fastighetsf\u00f6rmedling",
          "type": "Broker",
          "url": "http://www.svenskfast.se/"
        },
        "url": "https://www.booli.se/annons/2264953"
      },
      {
        "additionalArea": 0,
        "booliId": 2258574,
        "isNewConstruction": 1,
        "listPrice": 6850000,
        "livingArea": 129.5,
        "location": {
          "address": {
            "streetAddress": "Lyftsaxen"
          },
          "namedAreas": [
            "Enskede-\u00c5rsta-Vant\u00f6r"
          ],
          "position": {
            "latitude": 59.2826,
            "longitude": 18.0483
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Parhus",
        "plotArea": 0,
        "published": "2017-02-14 12:44:16",
        "rent": 3976,
        "rooms": 5,
        "source": {
          "id": 150830574,
          "name": "TryggHem Bostads AB",
          "type": "Construction",
          "url": "http://trygghem.se/"
        },
        "url": "https://www.booli.se/annons/2258574"
      },
      {
        "additionalArea": 0,
        "booliId": 2258570,
        "isNewConstruction": 1,
        "listPrice": 6850000,
        "livingArea": 129.5,
        "location": {
          "address": {
            "streetAddress": "Lyftsaxen"
          },
          "namedAreas": [
            "Enskede-\u00c5rsta-Vant\u00f6r"
          ],
          "position": {
            "latitude": 59.2826,
            "longitude": 18.0483
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Parhus",
        "plotArea": 0,
        "published": "2017-02-14 12:44:08",
        "rent": 3976,
        "rooms": 5,
        "source": {
          "id": 150830574,
          "name": "TryggHem Bostads AB",
          "type": "Construction",
          "url": "http://trygghem.se/"
        },
        "url": "https://www.booli.se/annons/2258570"
      },
      {
        "booliId": 2253735,
        "constructionYear": 2010,
        "floor": 0,
        "listPrice": 7600000,
        "listPriceChange": 650000,
        "listPriceChangeDate": "2017-02-24 23:04:12",
        "livingArea": 120,
        "location": {
          "address": {
            "streetAddress": "S\u00e5gverksgatan 41"
          },
          "namedAreas": [
            "Stureby"
          ],
          "position": {
            "latitude": 59.27624745,
            "longitude": 18.04955006
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Radhus",
        "published": "2017-02-06 12:33:53",
        "rent": 2600,
        "rooms": 5,
        "source": {
          "id": 1901865,
          "name": "MOHV",
          "type": "Broker",
          "url": "http://www.mohv.se/"
        },
        "url": "https://www.booli.se/annons/2253735"
      },
      {
        "booliId": 2219526,
        "isNewConstruction": 1,
        "listPrice": 6995000,
        "livingArea": 117,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal 2B \u2013 Kvarteret Minglet"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25690089,
            "longitude": 18.12765812
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-18 16:31:27",
        "rent": 32400,
        "rooms": 5,
        "source": {
          "id": 5804636,
          "name": "Veidekke Bostad AB",
          "type": "Construction",
          "url": "http://www.veidekkebostad.se/"
        },
        "url": "https://www.booli.se/annons/2219526"
      },
      {
        "booliId": 2219467,
        "isNewConstruction": 1,
        "listPrice": 7295000,
        "livingArea": 117,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal 2B \u2013 Kvarteret Minglet"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25690089,
            "longitude": 18.12765812
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-18 16:14:17",
        "rent": 32400,
        "rooms": 5,
        "source": {
          "id": 5804636,
          "name": "Veidekke Bostad AB",
          "type": "Construction",
          "url": "http://www.veidekkebostad.se/"
        },
        "url": "https://www.booli.se/annons/2219467"
      },
      {
        "booliId": 2219388,
        "isNewConstruction": 1,
        "listPrice": 8250000,
        "livingArea": 132,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal 2B \u2013 Kvarteret Minglet"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25690089,
            "longitude": 18.12765812
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-18 15:49:20",
        "rent": 34800,
        "rooms": 5,
        "source": {
          "id": 5804636,
          "name": "Veidekke Bostad AB",
          "type": "Construction",
          "url": "http://www.veidekkebostad.se/"
        },
        "url": "https://www.booli.se/annons/2219388"
      },
      {
        "booliId": 2219378,
        "isNewConstruction": 1,
        "listPrice": 6995000,
        "livingArea": 117,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal 2B \u2013 Kvarteret Minglet"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25690089,
            "longitude": 18.12765812
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-18 15:44:43",
        "rent": 32400,
        "rooms": 5,
        "source": {
          "id": 5804636,
          "name": "Veidekke Bostad AB",
          "type": "Construction",
          "url": "http://www.veidekkebostad.se/"
        },
        "url": "https://www.booli.se/annons/2219378"
      },
      {
        "booliId": 2219365,
        "isNewConstruction": 1,
        "listPrice": 7295000,
        "livingArea": 117,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal 2B \u2013 Kvarteret Minglet"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25690089,
            "longitude": 18.12765812
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-18 15:39:48",
        "rent": 32400,
        "rooms": 5,
        "source": {
          "id": 5804636,
          "name": "Veidekke Bostad AB",
          "type": "Construction",
          "url": "http://www.veidekkebostad.se/"
        },
        "url": "https://www.booli.se/annons/2219365"
      },
      {
        "booliId": 2219305,
        "isNewConstruction": 1,
        "listPrice": 7495000,
        "livingArea": 117,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal 2B \u2013 Kvarteret Minglet"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25690089,
            "longitude": 18.12765812
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-18 15:16:54",
        "rent": 32400,
        "rooms": 5,
        "source": {
          "id": 5804636,
          "name": "Veidekke Bostad AB",
          "type": "Construction",
          "url": "http://www.veidekkebostad.se/"
        },
        "url": "https://www.booli.se/annons/2219305"
      },
      {
        "booliId": 2219296,
        "isNewConstruction": 1,
        "listPrice": 7145000,
        "livingArea": 117,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal 2B \u2013 Kvarteret Minglet"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25690089,
            "longitude": 18.12765812
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-18 15:12:32",
        "rent": 32400,
        "rooms": 5,
        "source": {
          "id": 5804636,
          "name": "Veidekke Bostad AB",
          "type": "Construction",
          "url": "http://www.veidekkebostad.se/"
        },
        "url": "https://www.booli.se/annons/2219296"
      },
      {
        "booliId": 2219285,
        "isNewConstruction": 1,
        "listPrice": 6995000,
        "livingArea": 117,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal 2B \u2013 Kvarteret Minglet"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25690089,
            "longitude": 18.12765812
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-18 15:08:22",
        "rent": 32400,
        "rooms": 5,
        "source": {
          "id": 5804636,
          "name": "Veidekke Bostad AB",
          "type": "Construction",
          "url": "http://www.veidekkebostad.se/"
        },
        "url": "https://www.booli.se/annons/2219285"
      },
      {
        "booliId": 2219279,
        "isNewConstruction": 1,
        "listPrice": 6995000,
        "livingArea": 117,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal 2B \u2013 Kvarteret Minglet"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25690089,
            "longitude": 18.12765812
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-18 15:06:53",
        "rent": 32400,
        "rooms": 5,
        "source": {
          "id": 5804636,
          "name": "Veidekke Bostad AB",
          "type": "Construction",
          "url": "http://www.veidekkebostad.se/"
        },
        "url": "https://www.booli.se/annons/2219279"
      },
      {
        "booliId": 2219274,
        "isNewConstruction": 1,
        "listPrice": 7990000,
        "livingArea": 132,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal 2B \u2013 Kvarteret Minglet"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25690089,
            "longitude": 18.12765812
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-18 15:04:44",
        "rent": 34800,
        "rooms": 5,
        "source": {
          "id": 5804636,
          "name": "Veidekke Bostad AB",
          "type": "Construction",
          "url": "http://www.veidekkebostad.se/"
        },
        "url": "https://www.booli.se/annons/2219274"
      },
      {
        "booliId": 2219272,
        "isNewConstruction": 1,
        "listPrice": 6995000,
        "livingArea": 117,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal 2B \u2013 Kvarteret Minglet"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25690089,
            "longitude": 18.12765812
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-18 15:03:16",
        "rent": 28800,
        "rooms": 5,
        "source": {
          "id": 5804636,
          "name": "Veidekke Bostad AB",
          "type": "Construction",
          "url": "http://www.veidekkebostad.se/"
        },
        "url": "https://www.booli.se/annons/2219272"
      },
      {
        "booliId": 2210256,
        "constructionYear": 2017,
        "isNewConstruction": 1,
        "listPrice": 6700000,
        "livingArea": 129,
        "location": {
          "address": {
            "streetAddress": "Stora Sk\u00f6ndals v\u00e4g 27"
          },
          "namedAreas": [
            "Sk\u00f6ndal"
          ],
          "position": {
            "latitude": 59.2578854,
            "longitude": 18.1256875
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-03 21:14:13",
        "rent": 4988,
        "rooms": 5,
        "source": {
          "id": 713,
          "name": "Svensk Fastighetsf\u00f6rmedling",
          "type": "Broker",
          "url": "http://www.svenskfast.se/"
        },
        "url": "https://www.booli.se/annons/2210256"
      },
      {
        "booliId": 2210109,
        "constructionYear": 2017,
        "isNewConstruction": 1,
        "listPrice": 7500000,
        "livingArea": 147,
        "location": {
          "address": {
            "streetAddress": "Stora Sk\u00f6ndals v\u00e4g 42"
          },
          "namedAreas": [
            "Sk\u00f6ndal"
          ],
          "position": {
            "latitude": 59.2578854,
            "longitude": 18.1256875
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-11-03 19:19:57",
        "rent": 5551,
        "rooms": 6,
        "source": {
          "id": 713,
          "name": "Svensk Fastighetsf\u00f6rmedling",
          "type": "Broker",
          "url": "http://www.svenskfast.se/"
        },
        "url": "https://www.booli.se/annons/2210109"
      },
      {
        "booliId": 2121112,
        "isNewConstruction": 1,
        "listPrice": 6900000,
        "livingArea": 129,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25875386,
            "longitude": 18.12628004
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-06-04 00:35:02",
        "rent": 4988,
        "rooms": 5,
        "source": {
          "id": 419,
          "name": "Besqab",
          "type": "Construction",
          "url": "http://www.besqab.se/"
        },
        "url": "https://www.booli.se/annons/2121112"
      },
      {
        "booliId": 2121102,
        "isNewConstruction": 1,
        "listPrice": 6700000,
        "livingArea": 129,
        "location": {
          "address": {
            "streetAddress": "Lilla Sk\u00f6ndal"
          },
          "namedAreas": [
            "Farsta stadsdelsomr\u00e5de"
          ],
          "position": {
            "latitude": 59.25875386,
            "longitude": 18.12628004
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Kedjehus",
        "published": "2016-06-04 00:15:43",
        "rent": 4988,
        "rooms": 5,
        "source": {
          "id": 419,
          "name": "Besqab",
          "type": "Construction",
          "url": "http://www.besqab.se/"
        },
        "url": "https://www.booli.se/annons/2121102"
      },
      {
        "booliId": 2009996,
        "constructionYear": 1962,
        "livingArea": 100,
        "location": {
          "address": {
            "streetAddress": "Glanshammarsgatan 115"
          },
          "namedAreas": [
            "Ormk\u00e4rr"
          ],
          "position": {
            "latitude": 59.2615077,
            "longitude": 18.00130698
          },
          "region": {
            "countyName": "Stockholms l\u00e4n",
            "municipalityName": "Stockholm"
          }
        },
        "objectType": "Radhus",
        "plotArea": 201,
        "published": "2016-01-08 01:12:13",
        "rooms": 5,
        "source": {
          "id": 1517,
          "name": "M\u00e4klarcentrum",
          "type": "Broker",
          "url": "http://www.maklar-centrum.se/"
        },
        "url": "https://www.booli.se/annons/2009996"
      }
    ]""")
        return test