from typing import Any


class Logger:

    colors = {
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'cyan': 36,
        'gray': 37,
    }

    @classmethod
    def _log(cls, text: Any, color: str):
        print(f"\033[{cls.colors[color]}m{text}\033[0m")

    @classmethod
    def error(cls, text: Any):
        cls._log(text, "red")

    @classmethod
    def success(cls, text: Any):
        cls._log(text, "green")

    @classmethod
    def warning(cls, text: Any):
        cls._log(text, "yellow")

    @classmethod
    def strong(cls, text: Any):
        cls._log(text, "blue")

    @classmethod
    def info(cls, text: Any):
        cls._log(text, "cyan")

    @classmethod
    def debug(cls, text: Any):
        cls._log(text, "gray")
