import pymongo
import requests
import json
from api_to_mongo import Ship
from api_to_mongo import  Pilot
import unittest

class UnitTests:
    def __init__(self):
        print('initialising')
        self.Luke = Pilot("https://swapi.dev/api/people/1/")
        self.Falcon = Ship(requests.get('https://swapi.dev/api//starships/10/').json())

        self.check_pilots()
        self.check_starships()

    def check_pilots(self):
        if self.Luke.pilot['name'] == 'Luke Skywalker':
            print("Pilot class correctly found Luke Skywalker from API link")
        else:
            print("Found incorrect pilot, check Pilot class")
        return

    def check_starships(self):
        falcon_pilots = []
        for pilot in self.Falcon.starship['pilots']:
            pilot = Pilot(pilot)
            falcon_pilots.append(pilot.pilot['name'])
        if 'Han Solo' in falcon_pilots:
            print("Ships class correctly identified Han Solo as a pilot on the Millenium Falcon")
        else:
            print("Ships class failed to identify Han Solo as a pilot on the Millenium Falcon")
        self.Falcon.alter_pilots()

        falcon_pilots = self.Falcon.starship['pilots']
        i=0
        while True:
            if i>=len(falcon_pilots):
                print("Han Solo not correctly turned into MongoDB id")
                break
            elif "61e58b896c7bb37eaf8aba4c" in str(falcon_pilots[i]):
                print("Han Solo correctly turned into MongoDB id")
                break
            else:
                i+=1
        return


UnitTests()