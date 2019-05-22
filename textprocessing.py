import re  # Library for dealing with regular expressions
from functools import reduce

# This file contains functions for cleaning up a text, e.g. extracting all the words with all special characters removed.


def get_words(text):
    # Use regex to remove special characters from text and replace them with whitespaces
    cleaned_text = re.sub("[\W]{1,}", " ", text)

    # Split at whitespace
    text_list = re.split(" ", cleaned_text)

    return text_list


def expand_words(text):
    # Turn abbreviations into their full word counterparts, e.g. "there's" -> "there is"
    isified_text = re.sub("([\w])'(s)", r"\1 is", text)

    # "should've" -> "should have"
    haveified_text = re.sub("([\w])'(ve)", r"\1 have", isified_text)

    return haveified_text


def average_length(words):
    # Given a text, calculate the average length of all words
    text_length = reduce(lambda acc, word: acc + len(word), words, 0)
    number_of_words = len(words)
    return text_length / number_of_words


def clean_file(filename):
    file = open(filename, "r")
    file_text = file.read()
    return get_words(file_text)


print("Vanlig ord Svenska", average_length(clean_file("common_swedish.txt")))
print("Vanlig ord Engelska", average_length(clean_file("common_english.txt")))
print("Röda rummet Svenska: ", average_length(clean_file("roda_rummet.txt")))
print("Röda rummet Engelska: ", average_length(clean_file("red_room.txt")))

# print(clean_file("moby.txt"))
