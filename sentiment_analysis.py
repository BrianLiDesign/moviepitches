# sentiment_analysis.py
# Author: Brian Li
from textblob import TextBlob

genres_very_happy = ["action", "adventure", "comedy", "family", "fantasy", "musical", "romance"]
genres_happy = ["adventure", "game-show", "fantasy", "sport"]
genres_neutral = ["biography", "documentary", "news", "talk-show", "western"]
genres_negative = ["mystery", "crime", "film-noir", "thriller"]
genres_very_negative = ["adult", "crime", "horror", "film-noir", "thriller", "war"]

def sentiment_analysis(mood) -> str:
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

def set_genre(mood: str) -> list:
    if mood == "very happy":
        return genres_very_happy
    if mood == "happy":
        return genres_happy
    if mood == "neutral":
        return genres_neutral
    if mood == "negative":
        return genres_negative