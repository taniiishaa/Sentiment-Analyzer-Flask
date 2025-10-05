from flask import Flask, render_template, request
from textblob import TextBlob

# =================================================================
# 1. CORE LOGIC FUNCTION (MUST BE DEFINED BEFORE IT IS CALLED)
# This function is the intellectual core of the application.
# =================================================================

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text and categorizes it.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary containing the raw scores and the categorized sentiment.
    """
    # 1. Handle empty input gracefully
    if not text or not text.strip():
        return {
            "sentiment": "Neutral",
            "polarity": 0.0,
            "subjectivity": 0.0,
            "message": "Please enter text to analyze."
        }
        
    # 2. Create the TextBlob object
    analysis = TextBlob(text)
    
    # Extract polarity and subjectivity scores, rounded for clean display
    polarity_score = round(analysis.sentiment.polarity, 4)
    subjectivity_score = round(analysis.sentiment.subjectivity, 4)
    
    # 3. Implement Impressive Categorization Logic
    # Polarity must be above +0.15 or below -0.15 to be non-neutral (smart threshold)
    NEUTRAL_THRESHOLD = 0.15 

    if polarity_score > NEUTRAL_THRESHOLD:
        sentiment_category = "Positive"
    elif polarity_score < -NEUTRAL_THRESHOLD:
        sentiment_category = "Negative"
    else:
        sentiment_category = "Neutral"
        
    # 4. Return structured results
    return {
        "text_input": text,
        "sentiment": sentiment_category,
        "polarity": polarity_score,
        "subjectivity": subjectivity_score
    }

# =================================================================
# 2. FLASK APP SETUP AND ROUTES
# =================================================================

# Initialize the Flask application
app = Flask(__name__)

# Route for the Home Page (GET: Display the input form)
@app.route('/', methods=['GET'])
def index():
    # Renders the HTML template containing the text input form
    return render_template('index.html')

# Route for Analysis (POST: Receive text, analyze, and display results)
@app.route('/', methods=['POST'])
def analyze():
    # Get the text input from the submitted form data
    user_text = request.form.get('text_input', '') 
    
    # Call the core logic function (which is defined above this function)
    results = analyze_sentiment(user_text)
    
    # Render the results back to the user, passing the data to the template
    return render_template(
        'index.html', 
        # Pass back the results dictionary and the original text
        results=results,
        original_text=user_text
    )

if __name__ == '__main__':
    # Run the application (debug=True allows hot reloading during development)
    app.run(debug=True)
