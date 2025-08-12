from utils import Helper

def getIndexOfChar(word: str, char: str) -> list[int]:
    return [i for i, c in enumerate(word) if c == char]

def printFruit(fruit: str, list_index: list[int]) -> None:
    for i in range(len(fruit)):
        if i in list_index:
            print(fruit[i], end=' ')
        else:
            print('_', end=' ')
    print()

if __name__ == "__main__":
    words = Helper.getWordsFromFile("data/fruits.json")

    fruit = Helper.getRandomFruit(words)
    name = input("Enter your name: ")
    print(f'Hello {name}, good luck to you!')

    count = 6
    lst_char = []
    while count > 0:
        print(f'You have {count} attempts to guess the fruit.')
        printFruit(fruit, lst_char)

        char = input('Guess a letter: ').lower()

        list_index = getIndexOfChar(fruit, char)

        if list_index:
            print(f'Good job! The letter "{char}" is in the fruit.')
            lst_char.extend(list_index)
        else:
            print(f'Sorry, the letter "{char}" is not in the fruit.')
            count -= 1

        if set(lst_char) == set(range(len(fruit))):
            print(f'Congratulations {name}! You guessed the fruit: {fruit}')
            break

    if count == 0:
        print(f'Sorry {name}, you ran out of attempts. The fruit was: {fruit}')