import re
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary for text replacement
replacements = {
    "Google": "Google©",
    "Fugro": "Fugro B.V.",
    "Holland": "The Netherlands"
}

# Precompile regex pattern to match any of the target words
pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in replacements.keys()) + r')\b')

@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.json
    text = data.get('text', '')

    # Replace using a lambda to look up replacements
    converted_text = pattern.sub(lambda match: replacements[match.group(0)], text)

    return jsonify({"converted_text": converted_text})

if __name__ == '__main__':
    app.run(debug=True)
