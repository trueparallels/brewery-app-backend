from flask import Flask
from flask_restful import Resource, Api
from waitress import serve
from likes import Likes

app = Flask(__name__)
api = Api(app)

api.add_resource(Likes, '/likes/<int:brewery_id>')

if __name__ == '__main__':
  serve(app, host='0.0.0.0', port='5000')