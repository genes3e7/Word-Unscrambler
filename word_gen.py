import os
import enchant
import itertools


class Word_Gen:
    def __init__(self, input_letters: list):
        self.d = enchant.Dict("en_US")
        self.d2 = enchant.Dict("en_SG")
        self.hash_map = dict()
        self.input_letters = input_letters
        self.__generate()

    def get_by_no(self, n: int):
        output = f"No of Letters: {n}\n"

        for idx, word in enumerate(self.hash_map[n]):
            output += word + "\t"

            if idx % 10 == 9:
                output += "\n"

        return output + "\n"

    def get_length(self):
        return len(self.input_letters)

    def __test_word(self, word: str):
        return self.d.check(word) or self.d2.check(word)

    def __word(self, n: int):
        word = []

        for string in itertools.permutations(self.input_letters, n):
            to_check = "".join(string)
            if self.__test_word(to_check):
                word.append(to_check)

        return sorted(set(word))

    def __generate(self):
        for n in range(1, len(self.input_letters) + 1):
            self.hash_map[n] = self.__word(n)

    def __str__(self):
        output = ""

        for key in self.hash_map.keys():
            output += f"No of Letters: {key}\n"

            for idx, word in enumerate(self.hash_map[key]):
                output += word + "\t"

                if idx % 10 == 9:
                    output += "\n"

            output += "\n" * (2 if self.hash_map[key] else 1)

        return output


if __name__ == "__main__":
    again = "y"

    try:
        while again.casefold() == "y".casefold():
            inputs = input("Type all letters: ")
            inputs = sorted(char.lower() for char in inputs if char.isalpha())
            all_words = Word_Gen(inputs)

            # Print either words of length wanted or everything
            inputs = input(f"Type length between 1 and {all_words.get_length()} to print words of length\
                \nor anything else to print all: ")
            print("=" * 80 + "\n")
            try:
                print(all_words.get_by_no(int(inputs)))
            except:
                print(all_words)

            print("=" * 80 + "\n")
            again = input("Again ? (y / n): ")
            print("=" * 80 + "\n")
    except:
        pass
    finally:
        if os.name == "nt":
            os.system("pause")
