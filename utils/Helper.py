import random
from .FileHandling import FileHandling

class Helper:
    @staticmethod
    def getTopicChoice(topics: list[str]) -> str:
        print("Choose a topic:")
        for i, topic in enumerate(topics):
            print(f"{i + 1}. {topic}")
        choice = int(input("Enter the number of your choice: ")) - 1
        return topics[choice] if 0 <= choice < len(topics) else topics[0]

    @staticmethod
    def getWordsFromFile(file_path: str) -> list[str]:
        fruits = FileHandling.readJsonFile(file_path)
        return fruits if fruits is not None else []

    @staticmethod
    def getRandomFruit(fruits: list[str]) -> str:
        return random.choice(fruits)
    
    @staticmethod
    def getIndexOfChar(word: str, char: str) -> list[int]:
        return [i for i, c in enumerate(word) if c == char]

    @staticmethod
    def printFruit(fruit: str, list_index: list[int]) -> None:
        for i in range(len(fruit)):
            if i in list_index:
                print(fruit[i], end=' ')
            else:
                print('_', end=' ')
        print()
