from flask_restful import Resource
import boto3
import sys

class Likes(Resource):
  def __init__(self):
    self.session = boto3.Session()
    self.db = self.session.resource('dynamodb', region_name='us-east-1')
    self.table = self.db.Table('brewery-app-favorites-prod')

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

  def put(self, brewery_id):
    item = None

    try:
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
    except boto3.exceptions.botocore.exceptions.ClientError:
      response = self.table.put_item(
        Item={
          'BreweryId': brewery_id,
          'Likes': 1
        }
      )

      item = { 'Likes': 1 }


    return { "count": int(item['Likes'])}
