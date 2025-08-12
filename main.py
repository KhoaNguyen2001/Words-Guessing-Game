from config import Settings
from utils import Helper, IOHandling

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

        while True:
            char = input('Guess a letter: ').lower()
            if Helper.checkValidInput(char):
                break
            IOHandling.printError('Invalid input. Please enter a single alphabetical character.')

        list_index = Helper.getIndexOfChar(word, char)

        if list_index:
            IOHandling.printSuccess(f'Good job! The letter "{char}" is in the {topic}.')
            lst_char.extend(list_index)
        else:
            IOHandling.printWarning(f'Sorry, the letter "{char}" is not in the {topic}.')
            count -= 1

        if set(lst_char) == set(range(len(word))):
            IOHandling.printSuccess(f'Congratulations {name}! You guessed the {topic}: {word}')
            break

    if count == 0:
        IOHandling.printError(f'Sorry {name}, you ran out of attempts. The {topic} was: {word}')