def lambda_handler(event, context):
    # Extract information from the event (e.g., HTTP request payload)
    name = event.get('name', 'World')
    response = {
        "statusCode": 200,
        "body": f"Hello, {name}! This is a serverless response."
    }
    return response
