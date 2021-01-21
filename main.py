from init import *  # for init_data()
from complete import *


# @dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int

    def __init__(self, sentence, source, offset, score):
        self.completed_sentence = sentence
        self.source_text = source
        self.offset = offset
        self.score = score

    def __hash__(self):
        return hash((self.completed_sentence, self.source_text, self.offset, self.score))

    def auto_comp_print(self):
        print(f"{self.completed_sentence} (score: {self.score})")

    def get_score_of_obj(self):
        return self.score

    def get_sentence(self):
        return self.completed_sentence


def main():
    print("\nLoading the files and preparing the system...")
    data = init_data()
    print("The system is ready. ", end="")

    while 1:
        user_input = input("Enter your text:\n")

        if user_input == "":
            break

        while '#' not in user_input:
            res = get_best_k_completions(user_input, data)
            print(f"Here are {len(res)} suggestions:")

            for i, l in enumerate(res, 1):
                print(f"{i}.", end=" ")
                l.auto_comp_print()

            user_input += input(f"{user_input}")

    print("\nThank you for using our autocomplete\nGoodbye!!")


if __name__ == '__main__':
    main()
