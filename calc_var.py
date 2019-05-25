import re  # Library for dealing with regular expressions
import heapq
from functools import reduce
from textprocessing import get_words, clean_file, average_length


def calcVar(mean, words):
	sum=0
	for word in words:
		sum = sum + (len(word)-mean)**2
	return sum / len(words)


avg_swedish = average_length(clean_file("roda_rummet.txt"))
rodarummet = clean_file("common_swedish.txt")
avg_english = average_length(clean_file("red_room.txt"))
redroom = clean_file("common_english.txt")

var_swedish = calcVar(avg_swedish, rodarummet)
var_english = calcVar(avg_english, redroom)

stdev_swedish = var_swedish**(1/2)
stdev_english = var_english**(1/2)

print("Swedish VAR(X)= ", var_swedish)
print("English VAR(X)= ", var_english)

print("Swedish stdev=" , stdev_swedish)
print("English stdev=" , stdev_english)
