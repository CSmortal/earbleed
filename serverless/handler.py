import json
from apply_audio_fx import effect_audio

def process_audio(event, context):
    effect_audio(event['body'])
    f = open("temp-fx.ogg", "r")

    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }
    print(type(event["body"]))

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
