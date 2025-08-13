import time
from .IOHandling import IOHandling

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
    def exitGame():
        IOHandling.printSuccess("🩷 Thank you for playing! Goodbye!")
        time.sleep(1)
        exit(0)
