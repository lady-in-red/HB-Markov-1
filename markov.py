"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    text = contents.split()
    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    # iterating the string to get tuples to be set as keys and the following word
    # to be set at its value.
    for i in range(len(text_string) - 2):
        key1 = (text_string[i], text_string[i + 1])
        value1 = i + 2
        # if the tuple key is not in dictionary, add key, value
        if key1 not in chains:
            chains[key1] = [text_string[value1]]
        # if in dictionary, append to value list
        else:
            chains[key1].append(text_string[value1])
    # grab last two words in filestring ane make = to 1 tuple (-2, -1): {[None]}
    last_key = (text_string[-2], text_string[-1])
    # if in dictionary, append
    if last_key in chains:
        chains[last_key].append(None)
    # if not, create
    else:
        chains[last_key] = [None]
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    # pull random word from dictionary, add to list
    words.extend(choice(chains.keys()))
    # access tuple, find value (rand choose), add to list

    while True:
        # key = (words[-2], words[-1]))
        # possible_next = chains[key]
        # next_word = chosie(possible_next)
        next_word = choice(chains[(words[-2], words[-1])])
        if next_word is None or (len(" ".join(words)) > 140):
                                # and (
                                # words[-1][-1] == "." or
                                # words[-1][-1] == "?" or
                                # words[-1][-1] == "!" or
                                # words[-1][-1] == "\"" or
                                # words[-1][-1] == ")" or
                                # words[-1][-1] == "*")):
            break
        else:
            words.append(next_word)
    return " ".join(words)
    # make (y, z)
    # search dictionary for y, z
    # repeat until reach none.
    # change list into string


input_path = "brothers-grim.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
