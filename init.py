import os
import string

from trie import *


def edit_sentence(prefix: str) -> str:
    prefix = prefix.translate(str.maketrans('', '', string.punctuation))
    return ' '.join(prefix.lower().split())


def init_data():
    trie = Trie()
    init_trie(trie)
    return trie


def init_trie(trie):
    for line, path, line_num in uploading_files():
        line = edit_sentence(line)
        offset = 1
        while line != '':
            trie.insert(line, path, line_num, offset)
            line = line[1:]
            offset += 1


def uploading_files():
    for root, dirs, files in os.walk(f"./data"):
        for file in files:
            curr_path = f"./{root}/{file}"
            with open(curr_path) as file:
                for line_num, line in enumerate(file, 1):
                    yield line, curr_path, line_num



