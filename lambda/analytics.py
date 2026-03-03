import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener')

def lambda_handler(event, context):

    response = table.scan()

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(response['Items'])
    }
