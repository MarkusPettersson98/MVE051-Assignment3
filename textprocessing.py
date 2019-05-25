import re  # Library for dealing with regular expressions
from functools import reduce

# This file contains functions for cleaning up a text, e.g. extracting all the words with all special characters removed.


def get_words(text):
    # Use regex to remove special characters from text and replace them with whitespaces
    special_character_filter = "[^äåöÄÅÖéÉ\w]+" # Exclude nordic characters from regexp
    cleaned_text = re.sub(special_character_filter, " ", text)

    # Split at whitespace
    text_list = re.split(" ", cleaned_text)

    return text_list


def average_length(words):
    # Given a text, calculate the average length of all words
    text_length = reduce(lambda acc, word: acc + len(word), words, 0)
    number_of_words = len(words)
    return text_length / number_of_words


def clean_file(filename):
    file = open(filename, "r")
    file_text = file.read()
    return get_words(file_text)


# avg_len_common_swedish = average_length(clean_file("common_swedish.txt"))
# avg_len_common_english = average_length(clean_file("common_english.txt"))
# avg_len_red_swedish = average_length(clean_file("roda_rummet.txt"))
# avg_len_red_english = average_length(clean_file("red_room.txt"))


# print("Vanlig ord Svenska", avg_len_common_swedish)
# print("Vanlig ord Engelska", avg_len_common_english)
# print("Röda rummet Svenska: ", avg_len_red_swedish)
# print("Röda rummet Engelska: ", avg_len_red_english)
# print("Kvot vanliga ord (svenska / engelska): ",
#       avg_len_common_swedish / avg_len_common_english)
# print("Kvot röda rummet ord (svenska / engelska): ",
#       avg_len_red_swedish / avg_len_red_english)
