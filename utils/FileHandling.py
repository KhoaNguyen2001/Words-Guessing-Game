import typing
import json

class FileHandling:
    @staticmethod
    def readJsonFile(filepath: str) -> typing.Optional[list[str]]:
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return None