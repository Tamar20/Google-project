import linecache  # for getline()
from main import *


def get_best_k_completions(prefix: str, data: Trie):  # -> list[AutoCompleteData]:
    prefix = edit_sentence(prefix)
    return search_best_completions(prefix, data)


def get_sentences_from_path(path: str, line_num) -> str:
    with open(path, "r"):
        return linecache.getline(path, line_num)[:-1]


def search_best_completions(prefix: str, trie: Trie):
    complete_list = trie.search(prefix)
    auto_complete_set = set()

    for x in complete_list:
        x["score"] = get_score(len(prefix), len(prefix))

    if len(complete_list) < 5:
        complete_list += search_with_mistake(prefix, trie)

    for comp_dict in complete_list:
        sentence = get_sentences_from_path(comp_dict["path"], comp_dict["line_num"])
        auto_comp_obj = AutoCompleteData(sentence, comp_dict["path"], comp_dict["offset"], comp_dict["score"])
        auto_complete_set.add(auto_comp_obj)

    return sort_res_by_score(auto_complete_set)[:5]


def sort_res_by_score(auto_complete_list: set):
    complete_list = sorted(auto_complete_list, key=lambda obj: obj.get_score_of_obj(), reverse=True)

    return complete_list


def search_with_mistake(sentence: str, trie: Trie):
    return add_character(sentence, trie), delete_character(sentence, trie), replace_character(sentence, trie)


def add_character(sentence, trie: Trie):
    comp_list = []
    sentence_len = len(sentence)

    for index in range(sentence_len):
        for char in "abcdefghijklmnopqrstuvwxyz":
            comp_list_of_index = trie.search(sentence[:index] + char + sentence[index + 1:])
            for x in comp_list_of_index:
                x["score"] = get_score(sentence_len, index, "delete")
            comp_list += comp_list_of_index

    return comp_list


def delete_character(sentence, trie: Trie):
    comp_list = []
    sentence_len = len(sentence)

    for index in range(sentence_len):
        comp_list_of_index = trie.search(sentence[:index] + sentence[index + 1:])
        for x in comp_list_of_index:
            x["score"] = get_score(sentence_len, index, "delete")
        comp_list += comp_list_of_index

    return comp_list


def replace_character(sentence, trie: Trie):
    comp_list = []
    sentence_len = len(sentence)

    for index in range(sentence_len):
        for char in "abcdefghijklmnopqrstuvwxyz":
            comp_list_of_index = trie.search(sentence[:index] + char + sentence[index + 1:])
            for x in comp_list_of_index:
                x["score"] = get_score(sentence_len, index, "delete")
            comp_list += comp_list_of_index

    return comp_list


def get_score(sentence_len: int, different_character_index: int, complete_type: str = "simple"):
    score_map = {
        "simple": calculate_score_simple,
        "add": calculate_score_add,
        "delete": calculate_score_delete,
        "replacement": calculate_score_replace
    }
    return score_map[complete_type](sentence_len, different_character_index)


def calculate_score_simple(sentence_len, different_character_index):
    return sentence_len * 2


def calculate_score_add(sentence_len, different_character_index):
    if different_character_index < 4:
        minus = {0: 10, 1: 8, 2: 6, 3: 4}[different_character_index]
    else:
        minus = 2

    return sentence_len * 2 - minus


def calculate_score_delete(sentence_len, different_character_index):
    if different_character_index < 4:
        minus = {0: 10, 1: 8, 2: 6, 3: 4}[different_character_index]
    else:
        minus = 2

    return (sentence_len - 1) * 2 - minus


def calculate_score_replace(sentence_len, different_character_index):
    if different_character_index < 4:
        minus = {0: 5, 1: 4, 2: 3, 3: 2}[different_character_index]
    else:
        minus = 1

    return (sentence_len - 1) * 2 - minus
