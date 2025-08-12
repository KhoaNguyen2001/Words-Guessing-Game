from config import Settings
from utils import Helper

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(f'Hello {name}, good luck to you!')

    topic = Helper.getTopicChoice(Settings.LIST_DATA_FILE_PATH)
    words = Helper.getWordsFromFile(topic)

    word = Helper.getRandomWord(words)
    topic = Helper.getTopicFromPath(topic)
    count = Settings.MAX_ATTEMPTS
    lst_char = []

    while count > 0:
        print(f'You have {count} attempts to guess the {topic}.')
        Helper.printWord(word, lst_char)

        char = input('Guess a letter: ').lower()

        list_index = Helper.getIndexOfChar(word, char)

        if list_index:
            print(f'Good job! The letter "{char}" is in the {topic}.')
            lst_char.extend(list_index)
        else:
            print(f'Sorry, the letter "{char}" is not in the {topic}.')
            count -= 1

        if set(lst_char) == set(range(len(word))):
            print(f'Congratulations {name}! You guessed the {topic}: {word}')
            break

    if count == 0:
        print(f'Sorry {name}, you ran out of attempts. The {topic} was: {word}')