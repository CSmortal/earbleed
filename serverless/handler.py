
import json


def process_audio(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }
    print(type(event["body"]))

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response