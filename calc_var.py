import re  # Library for dealing with regular expressions
import heapq
from functools import reduce
from textprocessing import get_words, clean_file, average_length


def calcVar(mean, words):
	sum=0
	for word in words:
		sum = sum + (len(word)-mean)**2
	return sum / len(words)


clean_swedish=clean_file("common_swedish.txt")
clean_english=clean_file("common_english.txt")

mean_swedish = average_length(clean_swedish)
rodarummet = clean_file("roda_rummet.txt")
mean_english = average_length(clean_english)
redroom = clean_file("red_room.txt")

var_swedish = calcVar(mean_swedish, rodarummet)
var_english = calcVar(mean_english, redroom)

stdev_swedish = var_swedish**(1/2)
stdev_english = var_english**(1/2)

var_swedish_common = calcVar(mean_swedish, clean_swedish)
var_english_common = calcVar(mean_english, clean_english)

print()

print("Swedish röda rummet VAR(X)= ", var_swedish)
print("English red room VAR(X)= ", var_english)

print()

print("Swedish röda rummet stdev=" , stdev_swedish)
print("English red room stdev=" , stdev_english)

print()

print("swedish common VAR", var_swedish_common)
print("english common VAR", var_english_common)

print()

print("swedish common stdev=", var_swedish_common**(1/2))
print("english common stdev=", var_english_common**(1/2))

print()

