import inspect
import json
import pathlib
import re
import requests
import sys
from copy import copy
from dataclasses import dataclass
from typing import Any, Callable

from bs4 import BeautifulSoup
from dotenv import dotenv_values

from utilities.logger import Logger as log
from utilities.errors import WrongExampleAnswer, SubmissionError, IncorrectAnswer, KnownIncorrectAnswer, NotJSONSerializable


# Load cookies from .env
cookies: dict = dotenv_values(pathlib.Path(__file__).parent.parent / ".env")


# https://github.com/wimglenn/advent-of-code-data/blob/master/aocd/models.py#L380
WAIT: str = r"You have (?:(\d+)m )?(\d+)s left to wait"


# Use custom logger for custom exceptions
sys.excepthook = (
    lambda exception_type, exception, traceback, debug_hook=sys.excepthook:
    log.error(exception) if exception_type in (
        WrongExampleAnswer, SubmissionError, IncorrectAnswer, KnownIncorrectAnswer, NotJSONSerializable
    ) else debug_hook(exception_type, exception, traceback)
)


DEFAULT_CACHE: dict = {
    "1": {
        "correct": None,
        "incorrect": []
    },
    "2": {
        "correct": None,
        "incorrect": []
    }
}


@dataclass
class Puzzle:

    example_1: Any
    example_2: Any

    input_parse_line: Callable
    input_parse_overall: Callable

    def __post_init__(self):

        # Path, day, year, etc.
        self.path: pathlib.Path = pathlib.Path(inspect.stack()[2].frame.f_code.co_filename)

        self.file_name: str = self.path.stem
        self.day: str = self.file_name[3:]

        self.year_folder: pathlib.Path = self.path.parent.parent
        self.year: str = self.year_folder.stem

        # Load and parse input
        with open(f"{self.file_name}.txt") as file:
            self.input: list = self.input_parse_overall([self.input_parse_line(line.strip()) for line in file])

        # Load and parse example input
        with open(f"{self.file_name}_example.txt") as file:
            self.example: list = self.input_parse_overall([self.input_parse_line(line.strip()) for line in file])

    def solve(self, puzzle: int, solver: Callable) -> None:
        log.strong(f"Solving Puzzle {puzzle}...")

        # Check against example input
        example = solver(copy(self.example))
        if not example:
            return log.info("Skipping as puzzle solver is unfinished...")
        elif example != getattr(self, f"example_{puzzle}"):
            raise WrongExampleAnswer(incorrect=example, correct=getattr(self, f"example_{puzzle}"))

        # Solve puzzle
        answer = solver(copy(self.input))
        if not answer:
            return log.info("Skipping as puzzle solver is unfinished...")

        # Get current day/puzzle's cache
        cache: dict = self._cache().get(self.day, DEFAULT_CACHE)[str(puzzle)]

        # Not already submitted
        if cache.get("correct") is None:

            # Check incorrect answer cache
            if answer in cache.get("incorrect", []):
                raise KnownIncorrectAnswer(answer)

            # Submit answer to AoC website
            result: bool | None = self._submit_answer(puzzle, answer)

            # Successful
            if result is True:
                cache["correct"] = answer
                self._cache(self.day, puzzle, cache)
                log.success(f"Puzzle {puzzle} submitted successfully!")

            # Incorrect
            elif result is False:
                cache["incorrect"] = cache.get("incorrect", []) + [answer]
                self._cache(self.day, puzzle, cache)
                raise IncorrectAnswer(answer)

            # Error submitting
            elif result is None:
                raise SubmissionError(answer)

        else:
            log.info(f"Skipping Puzzle {puzzle} submission (already finished)")

        return answer

    @staticmethod
    def _json_serializable(obj: Any) -> bool:
        try:
            json.dumps(obj)
            return True
        except TypeError:
            return False

    def _cache(self, day: str = "100", puzzle: int = 1, updated: dict = None):

        # Read current cache
        with open(self.year_folder / ".cache.json", "r") as file:
            cache = json.load(file)

        # Update cache if applicable
        if updated:
            cache[day] = cache.get(day, DEFAULT_CACHE)
            cache[day].update({str(puzzle): updated})

            # Check serializability
            if not self._json_serializable(cache):
                raise NotJSONSerializable(cache)

            # Update json
            with open(self.year_folder / ".cache.json", "w") as file:
                json.dump(cache, file, indent=4)
                file.write("\n")

            log.debug("DEBUG: cache update successful")

        return cache

    def _submit_answer(self, part: int, answer: Any) -> bool | None:

        # POST response
        response = requests.post(
            url=f"https://adventofcode.com/{self.year}/day/{self.day}/answer",
            cookies=cookies,
            # headers={"User-Agent": "advent-of-code-data v1.1.1"},
            data={"level": part, "answer": str(answer)},
        )

        # Check if 200 OK
        if not response.ok:
            log.error(f"POST request failed!\n{response.status_code}: {response.text}")
            return None

        # Parse response text using bs4
        text = BeautifulSoup(response.text, "html.parser").article.text

        # Correct
        if "That's the right answer!" in text:
            return True

        # Already done
        elif "Did you already complete it" in text:
            log.warning("Warning: puzzle solution already completed")
            return True

        # Incorrect
        elif "That's not the right answer" in text:
            return False

        # Ratelimit
        elif "You gave an answer too recently" in text:
            [(m, s)] = re.findall(WAIT, text)
            log.error(f"Warning: puzzle submission ratelimited, try again in {m}m {s}s")
            return None

        log.debug(text)
        return None
