# main_tests.py
import unittest
import setup
import search_movies
import sentiment_analysis

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
        self.assertEqual(result, expected)


#Tests for search_movies
#Author: Natalie Cartwright
class TestSearchMovies(unittest.TestCase):
    #Tests the search_by_keyword function

    def test_search_by_genre(self):
        result = search_movies.search_by_genre("action")
        expected = [{'genre': 'action', 'length': 152, 'rating': 9.0, 'title': 'The Dark Knight'},
 {'genre': 'action', 'length': 148, 'rating': 8.8, 'title': 'Inception'},
 {'genre': 'action',
  'length': 124,
  'rating': 8.7,
  'title': 'Star Wars: Episode V - The Empire Strikes Back'},
 {'genre': 'action', 'length': 136, 'rating': 8.7, 'title': 'The Matrix'},
 {'genre': 'action', 'length': 207, 'rating': 8.6, 'title': 'Seven Samurai'},
 {'genre': 'action',
  'length': 110,
  'rating': 8.5,
  'title': 'Léon: The Professional'},
 {'genre': 'action', 'length': 155, 'rating': 8.5, 'title': 'Gladiator'},
 {'genre': 'action',
  'length': 137,
  'rating': 8.5,
  'title': 'Terminator 2: Judgment Day'},
 {'genre': 'action',
  'length': 149,
  'rating': 8.4,
  'title': 'Avengers: Infinity War'},
 {'genre': 'action', 'length': 137, 'rating': 8.4, 'title': 'Aliens'},
 {'genre': 'action', 'length': 120, 'rating': 8.4, 'title': 'Oldboy'},
 {'genre': 'action', 'length': 78, 'rating': 8.4, 'title': 'The General'},
 {'genre': 'action', 'length': 78, 'rating': 8.4, 'title': 'The General'},
 {'genre': 'action', 'length': 78, 'rating': 8.4, 'title': 'The General'}]
        self.assertEqual(result, expected)

    def test_search_by_genre2(self):
        result = search_movies.search_by_genre("python")
        expected = []
        self.assertEqual(result, expected)

    def test_search_by_title(self):
        result = search_movies.search_by_title("Star Wars")
        expected = [{'genre': 'action',
  'length': 124,
  'rating': 8.7,
  'title': 'Star Wars: Episode V - The Empire Strikes Back'}]
        self.assertEqual(result, expected)

    def test_search_by_title2(self):
        result = search_movies.search_by_title("Harry Potter")
        expected = []
        self.assertEqual(result, expected)

    def test_search_by_rating(self):
        result = search_movies.search_by_rating(9)
        expected = [{'genre': 'drama',
  'length': 142,
  'rating': 9.3,
  'title': 'The Shawshank Redemption'},
 {'genre': 'crime', 'length': 175, 'rating': 9.2, 'title': 'The Godfather'},
 {'genre': 'action', 'length': 152, 'rating': 9.0, 'title': 'The Dark Knight'},
 {'genre': 'crime',
  'length': 202,
  'rating': 9.0,
  'title': 'The Godfather Part II'},
 {'genre': 'drama', 'length': 96, 'rating': 9.0, 'title': '12 Angry Men'},
 {'genre': 'biography',
  'length': 195,
  'rating': 9.0,
  'title': "Schindler's List"}]
        self.assertEqual(result, expected)

    def test_search_by_rating2(self):
        result = search_movies.search_by_rating(10)
        expected = []
        self.assertEqual(result, expected)

    def test_search_by_length(self):
        result = search_movies.search_by_length(200)
        expected = [{'genre': 'crime',
  'length': 202,
  'rating': 9.0,
  'title': 'The Godfather Part II'},
 {'genre': 'fantasy',
  'length': 201,
  'rating': 8.9,
  'title': 'The Lord of the Rings: The Return of the King'},
 {'genre': 'action', 'length': 207, 'rating': 8.6, 'title': 'Seven Samurai'},
 {'genre': 'drama',
  'length': 238,
  'rating': 8.4,
  'title': 'Gone with the Wind'}]
        self.assertEqual(result, expected)

    def test_by_length2(self):
        result = search_movies.search_by_length(500)
        expected = []
        self.assertEqual(result, expected)


# Test setup.py validation functions
# Author: Brian Li
class TestInputValidation(unittest.TestCase):

    def test_validate_mood(self):
        self.assertTrue(setup.validate_mood("happy"))
    def test_validate_mood_empty(self):
        self.assertTrue(setup.validate_mood(""))
    def test_validate_mood_nums(self):
        self.assertFalse(setup.validate_mood("happy123"))
    def test_validate_mood_chars(self):
        self.assertFalse(setup.validate_mood("!happy"))
    def test_validate_mood_chars_2(self):
        self.assertFalse(setup.validate_mood("happy!"))

    def test_validate_number(self):
        self.assertTrue(setup.validate_number("150", 1, 180))
    def test_validate_number_min_bound(self):
        self.assertTrue(setup.validate_number("1", 1, 180))
    def test_validate_number_max_bound(self):
        self.assertTrue(setup.validate_number("180", 1, 180))
    def test_validate_number_below_min(self):
        self.assertFalse(setup.validate_number("0", 1, 180))
    def test_validate_number_above(self):
        self.assertFalse(setup.validate_number("200", 1, 180))
    def test_validate_number_string(self):
        self.assertFalse(setup.validate_number("abc", 1, 180))
    def test_validate_negative(self):
        self.assertFalse(setup.validate_number("-10", 1, 180))