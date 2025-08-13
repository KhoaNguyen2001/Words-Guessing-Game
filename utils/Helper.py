# File: utils/Helper.py

import random
from .FileHandling import FileHandling

class Helper:
    @staticmethod
    def getTopicFromPath(path: str) -> str:
        return path.split("/")[-1].split(".")[0].capitalize()

    @staticmethod
    def getWordsFromFile(file_path: str) -> list[str]:
        fruits = FileHandling.readJsonFile(file_path)
        return fruits if fruits is not None else []

    @staticmethod
    def getRandomWord(words: list[str]) -> str:
        return random.choice(words)

    @staticmethod
    def getIndexOfChar(word: str, char: str) -> list[int]:
        return [i for i, c in enumerate(word) if c == char]

    @staticmethod
    def printWord(word: str, list_index: list[int]) -> None:
        for i in range(len(word)):
            if i in list_index:
                print(word[i], end=' ')
            else:
                print('_', end=' ')
        print()

    @staticmethod
    def checkValidInput(char: str) -> bool:
        return len(char) == 1 and char.isalpha()