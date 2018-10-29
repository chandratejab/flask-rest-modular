from flask import Flask, Blueprint
from flask_restful import Api

from resources.todo import resources as todo_resources


app = Flask(__name__)
api = Api(app)


for r in todo_resources:
    api.add_resource(*r)

app.run(host='0.0.0.0', threaded=True)
