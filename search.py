import linecache
from main import *


def get_best_k_completions(prefix: str, data: Trie):  # -> list[AutoCompleteData]:
    prefix = edit_sentence(prefix)
    return search_best_completions(prefix, data)


def search_best_completions(prefix_list: str, trie: Trie):  # TODO: check type
    res = []
    tmp = trie.search(prefix_list)
    res += [get_sentences_from_path(p["path"], p["line_num"]) for p in tmp]
    res = set(res)
    res = list(res)  # TODO: sort by score
    return res[:5]


def get_sentences_from_path(path: str, line_num) -> str:
    with open(path, "r") as file:
        return linecache.getline(path, line_num)

