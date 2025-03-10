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
    def test_search_by_keyword(self):
        result = search_movies.search_by_keyword("cars")
        expected = ['Cars',
 'Cars 3',
 'Cars 2',
 'Z Cars',
 'Cars on the Road',
 'Used Cars',
 'Riding in Cars with Boys',
 'Comedians in Cars Getting Coffee',
 'Counting Cars',
 'The Cars That Ate Paris',
 'Hot Cars',
 'Cars of the Revolution',
 'Old Men in New Cars',
 'Stealing Cars',
 'Chasing Classic Cars',
 'Cars: The Video Game',
 'The Cars: You Might Think',
 'King of Cars',
 "Cars 3: Cars D'oeuvres",
 'Cars']
        self.assertEqual(result, expected)

        #Tests the search_by_title function
    def test_search_by_title(self):
        result = search_movies.search_by_title("Jurassic World")
        expected = ['Jurassic World: Rebirth',
 'Jurassic World',
 'Jurassic World: Dominion',
 'Jurassic World: Fallen Kingdom',
 'The Lost World: Jurassic Park',
 'Jurassic World: Chaos Theory',
 'Jurassic World: Camp Cretaceous',
 'Jurassic World Dominion: The Prologue',
 'Lego Jurassic World: Legend of Isla Nublar',
 'Jurassic World: The Ride',
 'Jurassic World: Blue',
 'Lego Jurassic World: The Indominus Escape',
 'Jurassic World: Fallen Kingdom - The Trailer Rescue',
 'Jurassic World Evolution 2',
 'Lego Jurassic World: The Secret Exhibit',
 'Lego Jurassic World: Double Trouble',
 'Exodus: Jurassic World Fan Film',
 'Lego Jurassic World',
 'Jurassic World Evolution',
 'From Jurassic Park to Jurassic World: Greatest Moments']
        self.assertEqual(result, expected)

    def test_search_by_rating(self):
        result = search_movies.search_by_rating(5)
        expected = []
        self.assertEqual(result, expected)

    def test_search_by_director(self):
        result = search_movies.search_by_director("Steve Spielberg")
        expected = ['Steve Spielberg',]
        self.assertEqual(result, expected)