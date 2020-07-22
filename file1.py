import json
import os
import string
import zipfile
import linecache  # for getline()


class Trie(object):
    def __init__(self):
        self.child = {}

    def insert(self, word, path):
        current = self.child
        for l in word:
            if l not in current:
                current[l] = {}
                current['/'] = []
            current['/'].append(path)
            current = current[l]

    def search(self, prefix):  # startsWith
        current = self.child
        for l in prefix:
            print(l)
            if l not in current:
                return False
            current = current[l]
        # return current['/']
        return [get_sentences_from_path(p) for p in current['/']]
        # return get_sentences_from_path(current['/'])


def get_sentences_from_path(path: str) -> str:
    path, line_num = get_path_and_line_num(path)
    with open(path, "r") as file:
        return linecache.getline(path, line_num)
        # return file.readline(line_num)


def get_path_and_line_num(path: str) -> tuple:
    line_num = ""
    while path[-1] != '/':
        line_num = path[-1] + line_num
        path = path[:-1]
    return path[:-1], int(line_num)


# def init():
#     data = load_files()


#    ...


# def init_trie(trie):  # load_files
#     with zipfile.ZipFile('technology_texts.zip') as folder:  # TODO: split function (with yield)
#         path = f"./{folder}"
#         for filename in folder.namelist():
#             path += f"/{filename}"
#             if not os.path.isdir(filename):
#                 with folder.open(filename) as file:
#                     path += f"/{file}"
#                     for i, line in enumerate(file, 1):
#                         trie.insert(edit_sentence(line), path + f"{i}")
#                         # edit line and insert to trie

def init_trie(trie):
    path = './python-3.8.4-docs-text/python-3.8.4-docs-text/bugs.txt'
    with open(path) as file:
        for line_num, line in enumerate(file, 1):
            trie.insert(edit_sentence(line), path + f"/{line_num}")


# def load_files():
#     #     with open('./python-3.8.4-docs-text/python-3.8.4-docs-text/bugs.txt') as json_file:
#     #         data = json.load(json_file)
#     data = {}
#     data["you"] = "Beyond just reporting bugs that you find, you are also welcome to submit patches to fix" \
#                   " them."
#     data["are"] = "Beyond just reporting bugs that you find, you are also welcome to submit patches to fix" \
#                   " them."
#     data[1] = "You can find more information on how to get started patching Python in the Python" \
#               " Developer's Guide."
#     data[2] = "If you have questions, the core-mentorship mailing list is a friendly place to get answers" \
#               " to any and all questions pertaining to the process of fixing issues in Python."
#     return data


# # @dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int


#     # methods that you need to define by yourself


def edit_sentence(prefix: str) -> str:
    prefix = prefix.translate(str.maketrans('', '', string.punctuation))
    return ' '.join(prefix.lower().split())


def search_best_completions(prefix_list: str, trie: Trie):  # TODO: check type
    res = []
    print(prefix_list)
    res.append(trie.search(prefix_list))

    return res


def get_best_k_completions(prefix: str, data: Trie):  # -> list[AutoCompleteData]:
    prefix = edit_sentence(prefix)
    print(prefix)
    # return find_5_best_comple
    return search_best_completions(prefix, data)


def init_data():
    data_trie = Trie()
    init_trie(data_trie)
    return data_trie


def main():
    print("hello")

    data = init_data()
    print(get_best_k_completions("Python", data))


if __name__ == '__main__':
    main()
