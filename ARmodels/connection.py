from library import MongoClient

client = MongoClient(host="localhost", port=27017)
db = client["air-quality"]
nairobi = db["nairobi"]