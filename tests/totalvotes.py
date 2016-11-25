#coding=utf-8
import unittest
from flask_pymongo import MongoClient
from bson.json_util import dumps
import json,urllib
# Instantiate mongo client
mongo = MongoClient()

# Create mongo database instance
db = mongo.datacentar

class VotesTestCases(unittest.TestCase):

    def setUp(self):
        pass

    def get_expcted_result(self):
        json_candidate=[{
            "izbornaLista":"АЛЕКСАНДАР ВУЧИЋ - СНС, СДПС, НС, СПО, ПС",
            "godina":2014,
            'teritorija':'ВОЈВОДИНА',
            'instanca':1,
            "rezultat":{
                "glasova":1736920,
                "udeo":"48.35"
            }
        }]
        return json_candidate

    def test_total_votes_candidates(self):
        for i in self.get_expcted_result():
            expected_votes=i['rezultat']['glasova']
            votes=db.izbori2.find({"izbornaLista":i['izbornaLista'],'godina':i['godina'],'teritorija':i['teritorija'],'instanca':i['instanca']},{"_id": 0})
        for total in votes:
            db_glasova=total['rezultat']['glasova']
        self.assertEqual(expected_votes,db_glasova)


