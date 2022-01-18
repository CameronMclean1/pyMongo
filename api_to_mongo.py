import pymongo
import requests
import json
from pprint import PrettyPrinter as pp

#Setting up mongo db connection
client = pymongo.MongoClient()
db = client['starWars']
db.starships.drop()
db.create_collection('starships')

class Pilot:
    '''Pilot class contains methods and information for pilots gathered from API
        Unlike Ship class Pilot generates itself from API link'''
    def __init__(self, link):
        self.pilot = requests.get(link).json()

    def get_id(self):
        name = self.pilot['name']
        id = db.characters.find({'name': name}, {'_id': 1})
        return(id[0])


class Ship:
    '''Ship class contains methods and information on starships collected from swapi
        API link must be processed elsewhere'''
    def __init__(self, starship):
        self.starship = starship
        self.alter_pilots()

    def alter_pilots(self):
        '''Changes the pilots from API links to ObjectIDs'''
        pilots = []
        for link in self.starship['pilots']:
            ship_pilot = Pilot(link)
            id = ship_pilot.get_id()
            pilots.append(id)
        self.starship['pilots'] = pilots
        return

    def write_to_starships(self):
        '''Adds ship to the starships collection'''
        db.starships.insert_one(self.starship)
        return


'''Command flow to append through ships'''
ships = requests.get('https://swapi.dev/api/starships/').json()
while ships != False:
    '''Ships changes to append through different pages
        When there is no other page to visit, ships=False'''
    for starship in ships['results']:
        starship = Ship(starship)
        starship.write_to_starships()

    try:
        ships = requests.get(ships['next']).json()
    except requests.exceptions.MissingSchema:
        ships = False


print('complete')