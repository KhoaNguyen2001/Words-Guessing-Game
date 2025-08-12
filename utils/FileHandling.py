# File utils/FileHandling.py - Handles file operations

import typing
import json
import os

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
        
    @staticmethod
    def getTopicPath(directory: str) -> typing.List[str]:
        """
        Get a list of topic file paths in the specified directory.

        Args:
            directory (str): The directory to search for topic files.

        Returns:
            typing.List[str]: A list of topic file paths.
        """
        return [os.path.join(directory, f).replace("\\", "/") for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]