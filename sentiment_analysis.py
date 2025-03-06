# sentiment_analysis.py
# Author: Brian Li
from textblob import TextBlob

def sentiment_analysis(mood):
    sentiment = TextBlob(mood).sentiment.polarity
    if sentiment > 0.5:
        return "very happy"
    elif 0.1 < sentiment <= 0.5:
        return "happy"
    elif 0.1 >= sentiment >= -0.1:
        return "neutral"
    elif -0.1 > sentiment >= -0.5:
        return "negative"
    else: # -0.5 > sentiment > -1.0
        return "very negative"

print(sentiment_analysis("happy"))
