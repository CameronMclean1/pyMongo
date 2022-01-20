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
        self.VaderShip = Ship(requests.get('https://swapi.dev/api//starships/13/').json())

        self.check_pilots()
        self.check_starships()

    def check_pilots(self):
        if self.Luke.pilot['name'] == 'Luke Skywalker':
            print("Pilot class correctly found Luke Skywalker from API link")
        else:
            print("Found incorrect pilot, check Pilot class")
        return

    def check_starships(self):
        VaderShip_pilots = []
        for pilot in self.VaderShip.starship['pilots']:
            pilot = Pilot(pilot)
            VaderShip_pilots.append(pilot.pilot['name'])
        if 'Darth Vader' in VaderShip_pilots:
            print("Ships class correctly identified Darth Vader as a pilot")
        else:
            print("Ships class failed to identify Darth Vader as a pilot")
        self.VaderShip.alter_pilots()

        VaderShip_pilots = self.VaderShip.starship['pilots']
        i=0
        while True:
            if i>=len(VaderShip_pilots):
                print("Darth Vader not correctly turned into MongoDB id")
                break
            elif "61e58b8140d779a8d6e04967" in str(VaderShip_pilots[i]):
                print("Darth Vader correctly turned into MongoDB id")
                break
            else:
                i+=1
        return


UnitTests()