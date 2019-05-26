import numpy as np
from textprocessing import clean_file, frequencies


def sort_dict(dictionary):
    return sorted(dictionary.items(), key=lambda key_value: key_value[0])


def frequencies_percentage(words):
    word_lenghts = np.array(list((map(len, words))))

    freq = frequencies(word_lenghts)
    sorted_freqs = sort_dict(freq)

    def calc_percentage(tup): return (
        tup[0], np.around(tup[1]/len(word_lenghts), 2))
    percentage_freqs = list(map(calc_percentage, sorted_freqs))
    return percentage_freqs


common_swedish = clean_file("common_swedish.txt")
common_english = clean_file("common_english.txt")
roda_rummet = clean_file("roda_rummet.txt")
red_room = clean_file("red_room.txt")

# Write frequencies to file
f = open("frequencies.txt", "a+")

f.write("Vanliga svenska ord \n")
f.write(str(frequencies_percentage(common_swedish)) + "\n")
f.write("Vanliga engelska ord \n")
f.write(str(frequencies_percentage(common_english)) + "\n")

f.write("Röda rummet \n")
f.write(str(frequencies_percentage(roda_rummet)) + "\n")
f.write("Red room \n")
f.write(str(frequencies_percentage(red_room)) + "\n")
