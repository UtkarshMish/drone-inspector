

from os import environ
from dotenv import load_dotenv
load_dotenv(".env")


DB_NAME = "drone_tracker"
HOST_IP = "localhost"
DB_PORT = 27017
SECRET_KEY = environ.get("SECRET_KEY")
DEBUG = True if environ.get("DEBUG") == 'true' else False