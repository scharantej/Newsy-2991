
# main.py

from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news_articles')
def get_news_articles():
    news_api_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY'
    response = requests.get(news_api_url)
    news_articles = response.json()['articles']

    # Save the news articles in the database

    return jsonify(news_articles)


if __name__ == '__main__':
    app.run(debug=True)
