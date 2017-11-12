import boto3
import json
import os


def get_secret():
    session = boto3.Session(aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
                            aws_secret_access_key=os.environ['AWS_SECRET_KEY'],
                            region_name=os.environ['AWS_REGION'])
    db = session.client('dynamodb')
    return json.dumps({'secret_code': db.query(TableName=os.environ['DYNAMO_TABLE'],
                                               ExpressionAttributeValues={
                                                   ':name': {
                                                       'S': os.environ['CODE_NAME'],
                                                   },
                                               }
                                               ,
                                       KeyConditionExpression='code_name = :name')['Items'][0]['secret_code']['S']})


def health():
    return json.dumps({'status': 'healthy', 'container': os.environ['HUB_URL'], 'project': os.environ['PROJECT_URL']})
