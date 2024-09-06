import ahocorasick
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary for text replacement
replacements = {
    "Google": "Google©",
    "Fugro": "Fugro B.V.",
    "Holland": "The Netherlands"
}

# Build the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add all the keys to the automaton
for key, value in replacements.items():
    A.add_word(key, (key, value))

# Finalize the automaton
A.make_automaton()

def aho_corasick_replace(text):
    output = []
    last_end = 0

    # Iterate over the matches in the text
    for end_index, (original_word, replacement) in A.iter(text):
        start_index = end_index - len(original_word) + 1
        
        # Append the text between the last match and this match
        output.append(text[last_end:start_index])
        
        # Append the replacement word
        output.append(replacement)
        
        # Update the last end position
        last_end = end_index + 1

    # Append the remaining part of the text
    output.append(text[last_end:])
    
    return ''.join(output)

@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.json
    text = data.get('text', '')

    # Use Aho-Corasick for efficient text replacement
    converted_text = aho_corasick_replace(text)

    return jsonify({"converted_text": converted_text})

if __name__ == '__main__':
    app.run(debug=True)
