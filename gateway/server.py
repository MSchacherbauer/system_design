import os
import gridfs
import pika
import json
from flask import Flask, request
from flask_pymongo import PyMongo


server = Flask(__name__)

# config
# MONGO_URI='mongodb://host.docker.internal:27017/videos'
server.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(server)
fs = gridfs.GridFS(mongo)

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()


@server.route("/login", methods=["POST"])
def login():
    token, err = access.login(request)


if __name__ == '__main__':
    server.run(host="0.0.0.0", port=5000)
