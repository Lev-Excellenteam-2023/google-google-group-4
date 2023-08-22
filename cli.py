import argparse
from get_complete_sentences import get_completions_for_user_input
from words_db import WordsDataBase


def main():
    parser = argparse.ArgumentParser(description="CLI Demo for Getting Completions")
    parser.add_argument("root_path", type=str, help="Path to the root directory containing text files")

    args = parser.parse_args()

    words_db = WordsDataBase(args.root_path)

    while True:
        user_input = input("Enter a user input (# to exit): ")
        if user_input == "#":
            break

        try:
            completions = get_completions_for_user_input(words_db, user_input)
            if completions:
                print("Completions:")
                for idx, completion in enumerate(completions, start=1):
                    print(f"{idx}. {completion}")
            else:
                print("No completions")
        except Exception as e:
            # print(f"An error occurred: {e}")
            print("No completions")


if __name__ == "__main__":
    main()
