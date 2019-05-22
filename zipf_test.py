import re  # Library for dealing with regular expressions
from functools import reduce

swedish_dictionary ={
}

english_dictionary ={
}


def get_words(text):
    # Use regex to remove special characters from text and replace them with whitespaces
    cleaned_text = re.sub("[\W]{1,}", " ", text)

    # Split at whitespace
    text_list = re.split(" ", cleaned_text)

    return text_list


def clean_file(filename):
    file = open(filename, "r")
    file_text = file.read()
    return get_words(file_text)


def initDictionary(arr, dictionary):
	for word in arr:
		lword = word.lower()
		if lword not in dictionary:
			dictionary[lword] = 0

def countOccur(words, dictionary):
	for word in words:
		lword = word.lower()
		if lword in dictionary:
			dictionary[lword] = dictionary[lword] + 1


initDictionary(clean_file("common_swedish.txt"), swedish_dictionary)
initDictionary(clean_file("common_english.txt"), english_dictionary)

countOccur(clean_file("roda_rummet.txt"), swedish_dictionary)
countOccur(clean_file("red_room.txt"), english_dictionary)

print("Svensk ordbok",swedish_dictionary)
print()
print("Engelsk ordbok", english_dictionary)