# sentiment_analysis.py
# Author: Brian Li
import data
from textblob import TextBlob


# The function performs sentiment analysis on the given mood text and classifies it into one of five categories:
# "very happy", "happy", "neutral", "negative", or "very negative".
# mood (str) argument is a string representing a mood description or phrase.
# The function returns a string indicating the sentiment of the input mood.

def sentiment_analysis(mood: str) -> str:
    sentiment = TextBlob(mood).sentiment.polarity
    if sentiment > 0.5:
        return "very positive"
    elif 0.1 < sentiment <= 0.5:
        return "positive"
    elif 0.1 >= sentiment >= -0.1:
        return "neutral"
    elif -0.1 > sentiment >= -0.5:
        return "negative"
    else: # -0.5 > sentiment > -1.0
        return "very negative"

# The function selects a list of movie genres based on the given mood category.
# mood (str) argument is a string representing a mood description or phrase
# The function returns a list of movie genres corresponding to the input mood, given from imported data.
def set_genre(mood: str) -> list:
    if mood == "very positive":
        return data.genres_very_positive
    if mood == "positive":
        return data.genres_positive
    if mood == "neutral":
        return data.genres_neutral
    if mood == "negative":
        return data.genres_negative
    if mood == "very negative":
        return data.genres_very_negative