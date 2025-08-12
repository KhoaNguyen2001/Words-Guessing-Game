import random
from .FileHandling import FileHandling

class Helper:
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
