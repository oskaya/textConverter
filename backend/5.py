import string
from flask import Flask, request, Response

app = Flask(__name__)

# Dictionary for text replacement
replacements = {
    "Google": "Google©",
    "Fugro": "Fugro B.V.",
    "Holland": "The Netherlands"
}

def replace_with_punctuation_handling(word):
    # Strip punctuation from the word
    stripped_word = word.strip(string.punctuation)

    # Replace the word if it exists in the dictionary
    replacement = replacements.get(stripped_word, stripped_word)

    # Preserve the original punctuation
    prefix = word[:len(word) - len(stripped_word)]  # Any prefix punctuation
    suffix = word[len(stripped_word):]  # Any suffix punctuation

    return prefix + replacement + suffix

def stream_convert_text():
    # Reading the request in chunks
    for chunk in request.stream:
        text = chunk.decode('utf-8')
        words = text.split()  # Split the text chunk into words
        converted_words = [replace_with_punctuation_handling(word) for word in words]
        converted_text = ' '.join(converted_words)  # Join words back into a chunk
        yield converted_text  # Stream the converted chunk back to the client

@app.route('/convert', methods=['POST'])
def convert_text():
    return Response(stream_convert_text(), content_type='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
