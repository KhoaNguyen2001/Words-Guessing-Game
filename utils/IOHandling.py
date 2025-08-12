class IOHandling:
    @staticmethod
    def printTextWithColor(text: str, color: str) -> None:
        color_codes = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "magenta": "\033[95m",
            "cyan": "\033[96m",
            "white": "\033[97m",
            "reset": "\033[0m"
        }
        print(f"{color_codes.get(color, color_codes['reset'])}{text}{color_codes['reset']}")

    @staticmethod
    def printError(text: str) -> None:
        IOHandling.printTextWithColor(text, "red")

    @staticmethod
    def printSuccess(text: str) -> None:
        IOHandling.printTextWithColor(text, "green")

    @staticmethod
    def printWarning(text: str) -> None:
        IOHandling.printTextWithColor(text, "yellow")
