import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby
from functools import reduce


from calc_var import calcVar, standard_deviation
from textprocessing import get_words, clean_file, average_length


def plot_words(words, title="Histogram of wordlength"):
    # words = array of words! E.g. already cleaned text
    # Calculate mean
    mean = average_length(words)

    # Calculate standard deviation
    stdev = standard_deviation(mean, words)

    # Gather data points
    word_lenghts = np.array(list((map(len, words))))

    # Prepare data
    mu = np.around(mean, 2)  # mean of distribution
    sigma = np.around(stdev, 2)  # standard deviation of distribution
    x = mu + sigma 

    fig, ax = plt.subplots()

    # the histogram of the data
    n, bins, patches = ax.hist(x)


    number_of_bars = range(1, max(word_lenghts), 1)
    plt.hist(word_lenghts, bins=number_of_bars, density=False, color="blue", ec='black')

    # # add a 'best fit' line
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

    # Plot all points
    # ax.plot(bins, y, '--')


    ax.set_xlabel('Word length')
    ax.set_ylabel('Density')
    ax.set_title(f'{title}: $\mu={mu}$, $\sigma={sigma}$')

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.show()


# Common words plots
plot_words(clean_file("common_swedish.txt"), "Historgram of wordlengths - common swedish words")
# plot_words(clean_file("common_english.txt"), "Historgram of wordlengths - common english words")


# # Strindbergs plots
# plot_words(clean_file("roda_rummet.txt"),   "Historgram of wordlengths - Red room (swedish)")
# plot_words(clean_file("red_room.txt"),      "Historgram of wordlengths - Red room (english)")
