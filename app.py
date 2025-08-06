# app.py

from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize the Flask app
app = Flask(__name__)

# Load the sentiment analysis pipeline from Hugging Face
# This model is downloaded the first time it's used.
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Define an API endpoint for prediction
@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    # Get the JSON data from the request
    data = request.get_json()
    
    # Check if 'text' is in the provided data
    if not data or 'text' not in data:
        return jsonify({"error": "Please provide 'text' in the request body."}), 400
        
    text_to_analyze = data['text']
    
    # Get the prediction from the model
    result = sentiment_analyzer(text_to_analyze)
    
    # Return the result as JSON
    return jsonify(result[0])

# Run the app
if __name__ == '__main__':
    # App will run on http://0.0.0.0:5000 inside the container
    app.run(host='0.0.0.0', port=5000)