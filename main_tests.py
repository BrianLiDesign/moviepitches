# main_tests.py
import unittest

import search_movies
import sentiment_analysis
# import search_movies


# Sentiment Analysis
# Author: Brian Li
class TestSentimentAnalysis(unittest.TestCase):
    def test_sentiment_analysis_very_positive(self):
        result = sentiment_analysis.sentiment_analysis("I loved my day!")
        expected = "very positive"
        self.assertEqual(result, expected)

    def test_sentiment_analysis_positive(self):
        result = sentiment_analysis.sentiment_analysis("i had a fun day")
        expected = "positive"
        self.assertEqual(result, expected)

    def test_sentiment_analysis_neutral(self):
        result = sentiment_analysis.sentiment_analysis("its alright.")
        expected = "neutral"
        self.assertEqual(result, expected)

    def test_sentiment_analysis_negative(self):
        result = sentiment_analysis.sentiment_analysis("I'm feeling sad right now")
        expected = "negative"
        self.assertEqual(result, expected)

    def test_sentiment_analysis_very_negative(self):
        result = sentiment_analysis.sentiment_analysis("THIS IS THE WORST")
        expected = "very negative"
        self.assertEqual(result, expected)

    def test_sentiment_analysis_no_emotion(self):
        result = sentiment_analysis.sentiment_analysis("Boat")
        expected = "neutral"
        self.assertEqual(result, expected)


# Author: Brian Li
class TestSetGenre(unittest.TestCase):
    def test_set_genre_very_positive(self):
        result = sentiment_analysis.set_genre("very positive")
        expected = ["action", "adventure", "comedy", "family", "fantasy", "musical", "romance"]
        self.assertEqual(result, expected)

    def test_set_genre_positive(self):
        result = sentiment_analysis.set_genre("positive")
        expected = ["adventure", "game-show", "fantasy", "sport"]
        self.assertEqual(result, expected)

    def test_set_genre_neutral(self):
        result = sentiment_analysis.set_genre("neutral")
        expected = ["biography", "documentary", "news", "talk-show", "western"]
        self.assertEqual(result, expected)

    def test_set_genre_negative(self):
        result = sentiment_analysis.set_genre("negative")
        expected = ["mystery", "crime", "film-noir", "thriller"]
        self.assertEqual(result, expected)

    def test_set_genre_very_negative(self):
        result = sentiment_analysis.set_genre("very negative")
        expected = ["adult", "crime", "horror", "film-noir", "thriller", "war"]


#Tests for search_movies
class TestSearchMovies(unittest.TestCase):
    #Tests the search_by_keyword function
    def test_search_by_genre(self):
        result = search_movies.search_by_genre("action")
        expected = []
        self.assertEqual(result, expected)

    def test_search_by_title(self):
        result = search_movies.search_by_title("Harry Potter")
        expected = []
        self.assertEqual(result, expected)

    def test_search_by_rating(self):
        result = search_movies.search_by_rating(5)
        expected = []
        self.assertEqual(result, expected)

    def test_search_by_length(self):
        result = search_movies.search_by_length(140)
        expected = []
        self.assertEqual(result, expected)


