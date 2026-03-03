import json
import boto3
import random
import string

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener')

def generate_short_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        original_url = body['url']

        short_id = generate_short_id()

        table.put_item(
            Item={
                'shortId': short_id,
                'originalUrl': original_url,
                'clicks': 0
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'shortId': short_id
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
