import time
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
    def exitGame():
        IOHandling.printSuccess("🩷 Thank you for playing! Goodbye!")
        time.sleep(1)
        exit(0)
