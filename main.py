from init import *
from trie import *
from search import *

# @dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int
    # methods that you need to define by yourself


def main():
    print("Loading the files and preparing the system...")
    data = init_data()
    user_input = input("The system is ready. Enter your text:\n")
    while '#' not in user_input :
        res = get_best_k_completions(user_input, data)
        print(f"Here are {len(res)} suggestions:")
        for i, l in enumerate(res, 1):
            print(f"{i}. {l}", end="")
        user_input += input(f"{user_input}")

    print("\nGoodbye!!")


if __name__ == '__main__':
    main()
