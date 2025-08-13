from utils import FileHandling

class Settings:
    MENU_ITEMS = ["Play Game", "View High Scores", "Exit"]
    LIST_DATA_FILE_PATH = FileHandling.getTopicPath("data/topics")
    STATISTICS_FILE_PATH = "data/storage/statistics.json"
    MAX_ATTEMPTS = 6