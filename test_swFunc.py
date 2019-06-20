#!/usr/bin/env python3

"""
 Author: David Addai
 This file tests the findLargest function of the swFunc module in accordance with the 
 test cases document in Google Docs.
"""


import unittest
import os.path
from swFunc import findLargest

# Modify this vairable with absolute path if running on a Windows machine
testDataPath = "./testData/"

class FindLargestTestCase(unittest.TestCase):
    """Tests for findLargest function"""

    def test_valid_path(self):
        """Successfully finds largest word when called with a valid file path containing words"""
        self.assertEqual("abcde", findLargest(os.path.join(testDataPath, "validFile.txt")))
    
    def test_filename_with_spaces(self):
        """Word found when called with a filename with spaces containing"""
        self.assertEqual("abcde", findLargest(os.path.join(testDataPath, "filename with spaces.txt")))
    
    def test_bad_path(self):
        """No word found when called with an non existant file path"""
        self.assertEqual(None, findLargest(os.path.join(testDataPath, "blah.txt")))

    def test_bad_path2(self):
        """No word found when called with a directory path"""
        self.assertEqual(None, findLargest(os.path.join(testDataPath, "")))
		
    def test_bad_path3(self):
        """No word found when called with a file where user has no read permissions"""
        self.assertEqual(None, findLargest(os.path.join(testDataPath, "validFileNoPermission.txt")))

    def test_file_with_single_word(self):
        """Word is found when file has a single word"""
        self.assertEqual("single", findLargest(os.path.join(testDataPath, "singleWordFile.txt")))

    def test_file_with_same_length_words(self):
        """Word is found when file has multiple largest words"""
        self.assertEqual("long", findLargest(os.path.join(testDataPath, "multipleLargest.txt")))

    def test_file_no_words(self):
        """No word found when file contains zero words"""
        self.assertEqual(None, findLargest(os.path.join(testDataPath, "noWords.txt")))

    def test_file_with_non_alpha_chars(self):
        """Word found when file contains non alpha characters"""
        self.assertEqual("!@#$%^&*()", findLargest(os.path.join(testDataPath, "nonAlphaChars.txt")))

    def test_file_with_single_char_word(self):
        """Word found when file has a single word with one character"""
        self.assertEqual("d", findLargest(os.path.join(testDataPath, "oneCharWord.txt")))

if __name__ == '__main__':
    unittest.main()
