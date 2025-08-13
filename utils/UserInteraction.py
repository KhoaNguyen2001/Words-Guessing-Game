import time

from .FileHandling import FileHandling
from .IOHandling import IOHandling
from .Helper import Helper

class UserInteraction:
    @staticmethod
    def getMenuChoice(items: list[str]) -> int:
        print("Please select an option from the menu:")
        for i, item in enumerate(items):
            print(f"{i + 1}. {item}")
        choice = int(input("Enter the number of your choice: ")) - 1
        if choice < 0 or choice >= len(items):
            IOHandling.printError("Invalid choice. Please try again.")
            return UserInteraction.getMenuChoice(items)
        return choice

    @staticmethod
    def getTopicChoice(topics: list[str]) -> str:
        print("Choose a topic:")
        for i, topic in enumerate(topics):
            print(f"{i + 1}. {Helper.getTopicFromPath(topic)}")
        choice = int(input("Enter the number of your choice: ")) - 1
        if choice < 0 or choice >= len(topics):
            IOHandling.printError("Invalid choice. Please try again.")
            return UserInteraction.getTopicChoice(topics)
        return topics[choice]
    
    @staticmethod
    def playGameInConsole(Settings):
        name = input("Enter your name: ")
        print(f'Hello {name}, good luck to you!')

        topic = UserInteraction.getTopicChoice(Settings.LIST_DATA_FILE_PATH)
        words = Helper.getWordsFromFile(topic)

        word = Helper.getRandomWord(words)
        topic = Helper.getTopicFromPath(topic)
        count = Settings.MAX_ATTEMPTS
        lst_char = []
        statistics_data = FileHandling.readJsonFile(Settings.STATISTICS_FILE_PATH)

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
        
        isWin = 1 if count > 0 else 0
        Helper.updateGameStatistics(statistics_data, isWin)

        FileHandling.writeJsonFile(Settings.STATISTICS_FILE_PATH, statistics_data)

    @staticmethod
    def viewHighScores(Settings):
        data = FileHandling.readJsonFile(Settings.STATISTICS_FILE_PATH)
        high_scores = data.get("high_scores", {})
        if high_scores:
            print("High Scores:")
            for name, score in high_scores.items():
                print(f"{name}: {score}")
        else:
            IOHandling.printError("No high scores available.")

    @staticmethod
    def exitGame():
        IOHandling.printSuccess("🩷 Thank you for playing! Goodbye!")
        time.sleep(1)
        exit(0)
