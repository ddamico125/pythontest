import json
import datetime
import boto3


def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}


dynamodb = boto3.resource('dynamodb')

def get(event, context):
  table = dynamodb.Table('test_user_tabel')

    # fetch todo from the database
    result = table.get_item(
      Key={
      'id': event['pathParameters']['id']
      }
      )

    # create a response
    response = {
    "statusCode": 200,
    "body": "body",
    }

    return response
