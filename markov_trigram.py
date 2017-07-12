"""TRY-Grams"""

from random import choice

def open_sesame(file_path):
    """Take file path, return as text string"""

    #open and parse file
    contents = open(file_path).read()
    text = contents.split()
    return text


def make_tri_chains(text_string):
    """Add tri_chain to dictionary with values."""

    chains = {}

    for i in range(len(text_string) - 3):
        key = (text_string[i], text_string[i + 1], text_string[i + 2])
        value = text_string[i + 3]

        if key not in chains:
            chains[key] = [value]

        else:
            chains[key].append(value)

    last_key = (text_string[-3], text_string[-2], text_string[-1])

    if last_key in chains:
        chains[last_key].append(None)

    else:
        chains[last_key] = [None]
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # grabs the keys in chains dictionary and adds random selection to list
    words.extend(choice(chains.keys()))

    while True:
        next_word = choice(chains[(words[-3], words[-2], words[-1])])
        if next_word is None or (words[-1][-1] == "." or
                                 words[-1][-1] == "?" or
                                 words[-1][-1] == "!" or
                                 words[-1][-1] == "\"" or
                                 words[-1][-1] == ")" or
                                 words[-1][-1] == "*"):
                                #(len(" ".join(words)) > 140):
            break
        else:
            words.append(next_word)
    # return words in string with each variable separated by a space
    return " ".join(words)

input_path = "brothers-grim.txt"

# Open the file and turn it into one long string
input_text = open_sesame(input_path)

# Get a Markov chain
chains = make_tri_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
