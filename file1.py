import json
import string


class Trie(object):
    def __init__(self):
        self.child = {}

    def insert(self, word):
        current = self.child
        for l in word:
            if l not in current:
                current[l] = {}
            current = current[l]
        # current['#'] = 1

    def search(self, prefix):  # startsWith
        current = self.child
        for l in prefix:
            if l not in current:
                return False
            current = current[l]
        return True

def init():
    data = load_files()
#    ...


def load_files():
    with zipfile.ZipFile('technology_texts.zip') as folder:
        for filename in folder.namelist():
            if not os.path.isdir(filename):
                with folder.open(filename) as file:
                    for line in file:
                        # edit line and insert to trie
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


def edit(prefix: str) -> list:
    prefix = prefix.translate(str.maketrans('', '', string.punctuation))
    return prefix.lower().split()


def search_best_completions(prefix_list: list):
    data = load_files()  # from file or data structure(dictionary)
    prefix_str = " ".join(prefix_list)
    res = []
    for row in data.keys():
        if prefix_str in data[row].lower():
            res.append(data[row])
    return res


def get_best_k_completions(prefix: str):  # -> list[AutoCompleteData]:
    #     return []
    prefix_list = edit(prefix)
    print(prefix_list)
    # return find_5_best_comple
    return search_best_completions(prefix_list)


def main():
    print("hello")
    data = load_files()
    print(get_best_k_completions("You ,are"))


if __name__ == '__main__':
    main()
