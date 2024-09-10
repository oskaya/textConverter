import re
import json
import config

replacements=config.replacements
pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in replacements.keys()) + r')\b')

def lambda_handler(event, context):
    print(event)
    if event['requestContext']['http']['method'] == 'POST':
        body = json.loads(event['body'])
        text = body["text"]
        converted_text = pattern.sub(lambda match: replacements[match.group(0)], text)
        print(converted_text)    
    return {"converted_text": converted_text}



