from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["audio_transcriptions"]
collection = db["transcripts"]