class MongoUtils(object):
    mongo = None

    def __init__(self, mongo):
        self.mongo = mongo
        self.izbori2 = "izbori2"

    def findResult(self):
        result = self.mongo.db[self.izbori2].find()
        return result
