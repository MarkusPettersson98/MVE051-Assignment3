import re  # Library for dealing with regular expressions

# This file contains functions for cleaning up a text, e.g. extracting all the words with all special characters removed.


def cleanText(text):
    # Use regex to remove special characters from text and replace them with whitespaces
    cleanedText = re.sub("[\W]{1,}", " ", text)
    
    # Split at whitespace
    textList = re.split(" ", cleanedText)

    return textList

def cleanFile(filename):
    file = open(filename, "r")
    fileText = file.read()
    return cleanText(fileText)


print(cleanFile("moby.txt"))
