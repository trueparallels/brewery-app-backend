from flask_restful import Resource
import boto3

class Likes(Resource):
  def __init__(self):
    self.session = boto3.Session(profile_name='kyle-sa')
    self.db = self.session.resource('dynamodb', region_name='us-east-1')
    self.table = self.db.Table('brewery-app-favorites-prod')

  def get(self, brewery_id):
    response = self.table.get_item(
      Key={
        'BreweryId': brewery_id
      }
    )

    item = response['Item']

    return { "count": int(item['Likes']) }

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
