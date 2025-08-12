# File utils/FileHandling.py - Handles file operations

import typing
import json

class FileHandling:
    """
    Handles file operations.
    """

    @staticmethod
    def readJsonFile(filepath: str) -> typing.Optional[list[str]]:
        """
        Reads a JSON file and returns the content as a list of strings.

        Args:
            filepath (str): The path to the JSON file.

        Returns:
            typing.Optional[list[str]]: A list of strings read from the JSON file, or None if an error occurs.
        """
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return None