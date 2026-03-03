import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener')

def lambda_handler(event, context):

    short_id = event['pathParameters']['shortId']

    response = table.get_item(Key={'shortId': short_id})

    if 'Item' not in response:
        return {
            'statusCode': 404,
            'body': 'URL not found'
        }

    item = response['Item']

    table.update_item(
        Key={'shortId': short_id},
        UpdateExpression='SET clicks = clicks + :inc',
        ExpressionAttributeValues={':inc': 1}
    )

    return {
        'statusCode': 302,
        'headers': {
            'Location': item['originalUrl']
        }
    }
