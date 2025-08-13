from utils import FileHandling

class Settings:
    MENU_ITEMS = ["Play Game", "View High Scores", "Exit"]
    LIST_DATA_FILE_PATH = FileHandling.getTopicPath("data/topics")
    MAX_ATTEMPTS = 6