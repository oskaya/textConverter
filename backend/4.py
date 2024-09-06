from flask import Flask, request, jsonify
from flask_cors import CORS  
from utilities.logging_utils import JsonFormatter
import re
import logging


#Customize logging with a custom formatter
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setFormatter(JsonFormatter()) 
logger.addHandler(console_handler)


app = Flask(__name__)
CORS(app)  


replacements = {
    "Google": "Google©",
    "Fugro": "Fugro B.V.",
    "Holland": "The Netherlands"
}

pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in replacements.keys()) + r')\b')

@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.json
    text = data.get('text', '')
    converted_text = pattern.sub(lambda match: replacements[match.group(0)], text)

    return jsonify({"converted_text": converted_text})

if __name__ == '__main__':
    app.run(debug=True)


