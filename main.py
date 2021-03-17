import requests
from flask import Flask
from flask_restplus import Resource, Api
from search.utils import pretty_print
from search.nlp import NLP
from search.query import Query

app = Flask(__name__)
api = Api(app, version='1.0', title="API backend for Search")


@api.route('/query/<string:query>')
class UserQuery(Resource):
    def get(self, query):
        q = Query(query)
        response = q.response()
        return response


if __name__ == '__main__':
    app.run()
