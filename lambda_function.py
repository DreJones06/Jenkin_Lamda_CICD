def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda, This is CICD pipeline example!'
    }
