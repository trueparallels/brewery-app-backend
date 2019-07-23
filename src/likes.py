from flask_restful import Resource
from flask_restful.utils import cors
import boto3
import sys

class Likes(Resource):
  def __init__(self):
    self.session = boto3.Session()
    self.db = self.session.resource('dynamodb', region_name='us-east-1')
    self.table = self.db.Table('brewery-app-favorites-prod')

  @cors.crossdomain(origin='*')
  def get(self, brewery_id):
    try:
      response = self.table.get_item(
      Key={
        'BreweryId': brewery_id
      }
    )
    except Exception as e:
      sys.exit(e)

    item = response['Item']

    return { "count": int(item['Likes']) }

  @cors.crossdomain(origin='*')
  def put(self, brewery_id):
    response = self.table.update_item(
      Key={
        'BreweryId': brewery_id
      },
      UpdateExpression='SET Likes = Likes + :inc',
      ExpressionAttributeValues={
        ':inc': 1
      },
      ReturnValues='UPDATED_NEW'
    )

    item = response['Attributes']

    return { "count": int(item['Likes'])}
