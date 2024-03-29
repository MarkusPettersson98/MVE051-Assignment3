import re  # Library for dealing with regular expressions
import heapq
from functools import reduce
from textprocessing import get_words, clean_file

swedish_dictionary ={
}

english_dictionary ={
}

# populates given dictionary with unique words in arr.
def initDictionary(arr, dictionary):
	for word in arr:
		lword = word.lower()
		if lword not in dictionary:
			dictionary[lword] = 0

# counts occurences of words in the dictionary.
def countOccur(words, dictionary):
	for word in words:
		lword = word.lower()
		if lword in dictionary:
			dictionary[lword] = dictionary[lword] + 1

# something i found on stackoverflow, do not touch! 
#def printMostUsed(dictionary, number):
#	maximums = {k: dictionary[k] for k in heapq.nlargest(number, dictionary, key=lambda k: dictionary[k])}
#	print(maximums)

initDictionary(clean_file("common_swedish.txt"), swedish_dictionary)
initDictionary(clean_file("common_english.txt"), english_dictionary)

countOccur(clean_file("roda_rummet.txt"), swedish_dictionary)
countOccur(clean_file("red_room.txt"), english_dictionary)

#printMostUsed(swedish_dictionary,10)
#printMostUsed(english_dictionary,10)

print("Svensk ordbok",swedish_dictionary)
print()
print("Engelsk ordbok", english_dictionary)