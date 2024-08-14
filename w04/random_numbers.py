from random import choice, uniform

def main():
    numbers = [16.2, 75.1, 52.3]
    print("numbers", numbers)
    append_random_numbers(numbers)
    print("numbers", numbers)
    append_random_numbers(numbers, 3)
    print("numbers", numbers)

    words = ["tomato", "potato", "carrot"]
    print("words", words)
    append_random_words(words)
    print("words", words)
    append_random_words(words, 3)
    print("words", words)

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        numbers_list.append(round(uniform(0, 100), 1))

def append_random_words(words_list, quantity=1):
    list_of_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    for _ in range(quantity):
        words_list.append(choice(list_of_words))


if __name__ == "__main__":
    main()
