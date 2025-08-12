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