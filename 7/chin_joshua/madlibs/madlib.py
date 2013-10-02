import re
import random
import markovchain

def main(text_name='Alice.txt', words=100):
    text = None
    with open(text_name) as file:
        text = "".join(file)
    word_list = re.split("\s+", text)
    words_to_pos = lookup(word_list)
    pos_to_words = invert(words_to_pos)
    chain = markovchain.MarkovChain(text)
    markov_out = list(chain._generate(words))
    for index, word in enumerate(markov_out):
        if word in words_to_pos:
            if random.random() < .2:
                pos = words_to_pos[word]
                replacement = random.choice(pos_to_words[pos])
                markov_out[index] = replacement
    return " ".join(markov_out)

def initialize(func):
    return func()

@initialize
def part_of_speech(dictionary_name='dictionary.txt'):
    entries = None
    with open(dictionary_name) as dictionary:
        entries = dictionary.readlines()
    dictionary = {}
    for entry in entries:
        entry = entry.strip()
        temp = re.split(r"\s+", entry)
        if len(temp) > 2:
            continue
        word, pos = temp
        pos=pos[0]
        if pos == 'C' or pos == 'D' or pos == 'P' or pos == 'r':
            continue
        dictionary[word]=pos[0]
    return dictionary

def lookup(word_list):
    return {word:part_of_speech[word]
     for word in word_list
     if word in part_of_speech}

def invert(dictionary):
    out = {}
    for key, value in dictionary.items():
        if value in out:
            out[value].append(key)
        else:
            out[value]=[key]
    return out
