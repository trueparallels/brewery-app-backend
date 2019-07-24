from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from waitress import serve
from likes import Likes
from healthcheck import HealthCheck

app = Flask(__name__)
api = Api(app)
CORS(app, origins='*')

api.add_resource(Likes, '/likes/<int:brewery_id>')
api.add_resource(HealthCheck, '/ok')

if __name__ == '__main__':
  serve(app, host='0.0.0.0', port='80')