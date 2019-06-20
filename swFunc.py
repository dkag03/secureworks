#!/usr/bin/env python3

"""
 Author: David Addai
 This application performs the following actions when called with a file path
# 1. Read input from a file of words;
# 2. Find the largest word in the file
# 3. Transpose the letters in the largest word
# 4. Show the largest word and the largest word transposed 
"""

import os.path
import sys
import errno

def findLargest(filePath = None):
    """Find and print the largest word from a file containing words.
    filePath:
        filePath: path to a text file
    Returns:
        The longest word in the file or None if word was not obtained
    """
    if not filePath:
        filePath = input("Please enter a file path ('q' to quit): ")
    if os.path.exists(filePath):
        try:
            f = open(filePath, 'r')
            wordList = [word for word in f.readlines() if word.strip() != '']
            f.close()
            # stop execution and notify user if the provided file is blank
            if len(wordList) == 0: 
                print ("File contains no words\n")
            else:
                longest = max(wordList, key=len)
                print(f'{longest.strip()}\n{longest[::-1].strip()}\n\n')
                return longest.strip()
        except IOError as e:
            print(f'Failed to open file: {os.strerror(e.errno)}')
    elif filePath.lower() != 'q': # stop execution and notify user if file path is invalid
        print(f"Invalid file path '{filePath}'\n") 


if __name__ == "__main__":
    if len(sys.argv) > 1:
        findLargest(sys.argv[1])
    else:
        findLargest()
        
