from config import Settings
from utils import UserInteraction

if __name__ == "__main__":
    while True:
        choice = UserInteraction.getMenuChoice(Settings.MENU_ITEMS)
        if choice == 0:
            UserInteraction.playGameInConsole(Settings)
        elif choice == 1:
            UserInteraction.viewHighScores(Settings)
        elif choice == 2:
            UserInteraction.exitGame()