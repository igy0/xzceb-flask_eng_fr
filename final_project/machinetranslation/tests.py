import unittest
import machinetranslation
from machinetranslation.translator import french_to_english, english_to_french

class TestFRtoEN(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('Bonjour'),None)

class TestENtoFR(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Hello'),None)

unittest.main()