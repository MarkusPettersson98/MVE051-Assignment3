import re  # Library for dealing with regular expressions
from functools import reduce
# This file contains functions for cleaning up a text, e.g. extracting all the words with all special characters removed.

text_path = "texts/"

def get_words(text):
    # Use regex to remove apostrophes and concatenate affected words
    apostrophes_filter = "'+"
    partially_cleaned_text = re.sub(apostrophes_filter, "", text)
    # Use regex to remove special characters from text and replace them with whitespaces
    special_character_filter = "[^äåöÄÅÖéÉ\w]+" # Exclude nordic characters from regexp
    cleaned_text = re.sub(special_character_filter, " ", partially_cleaned_text)

    # Split at whitespace
    text_list = re.split(" ", cleaned_text)

    return text_list


def average_length(words):
    # Given a text, calculate the average length of all words
    text_length = reduce(lambda acc, word: acc + len(word), words, 0)
    number_of_words = len(words)
    return text_length / number_of_words

def frequencies(coll):
    # Count how many times an item shows up in a collection
    output = {}
    for item in coll:
        if item not in output:
            output[item] = 0
        output[item] += 1
    return output


def clean_file(filename):
    file = open(text_path + filename, "r")
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
