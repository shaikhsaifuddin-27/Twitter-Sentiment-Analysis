import os
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
from flask import Flask, render_template, request, flash
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Flash messages

def analyze_sentiment(tweets):
    sentiment_results = {'positive': 0, 'neutral': 0, 'negative': 0}

    for tweet in tweets:
        analysis = TextBlob(tweet.strip())
        # Debugging: Print the polarity for each tweet
        print(f"Tweet: {tweet} | Polarity: {analysis.sentiment.polarity}")

        if analysis.sentiment.polarity > 0.1:  # Adjusted threshold for positivity
            sentiment_results['positive'] += 1
        elif analysis.sentiment.polarity < -0.1:  # Adjusted threshold for negativity
            sentiment_results['negative'] += 1
        else:
            sentiment_results['neutral'] += 1

    return sentiment_results

def visualize_sentiment(sentiment_results):
    labels = sentiment_results.keys()
    sizes = sentiment_results.values()
    colors = ['#66c2a5', '#fc8d62', '#8da0cb']

    plt.figure(figsize=(12, 6))

    # Bar chart
    plt.subplot(1, 2, 1)
    sns.barplot(x=labels, y=sizes, palette=colors)
    plt.title('Sentiment Analysis - Bar Chart')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')

    # Pie chart
    plt.subplot(1, 2, 2)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('Sentiment Analysis - Pie Chart')

    plt.tight_layout()  # Adjust the layout to prevent overlap
    plt.savefig('static/results.png')
    plt.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error_message = None

    if request.method == 'POST':
        tweets_input = request.form['tweets'].strip()

        if not tweets_input:
            error_message = "Please enter at least one tweet."
        else:
            tweets = tweets_input.splitlines()
            result = analyze_sentiment(tweets)
            visualize_sentiment(result)
            flash("Sentiment analysis completed successfully!")

    return render_template('index.html', result=result, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
