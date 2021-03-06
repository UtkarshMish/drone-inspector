

from os import environ

DB_NAME = "drone_tracker"
HOST_IP = environ.get("HOST_IP")
DB_PORT = 27017
SECRET_KEY = environ.get("SECRET_KEY")
DEBUG = True if environ.get("DEBUG") == 'true' else False
MONGO_URI = environ.get("CONNECTION_URI")
