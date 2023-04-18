import math
import random
import re
from typing import List

import click
from loguru import logger

MAX_SIZE_WORD = 9
MIN_SIZE_WORD = 2


class FilePaths:
    FRENCH = "dictionaries/french_common_words.txt"
    ENGLISH = "dictionaries/english_common_words.txt"


def is_valid(word: str) -> bool:
    if len(word) >= MAX_SIZE_WORD:
        return False
    if len(word) <= MIN_SIZE_WORD:
        return False
    if bool(re.search(r"[À-ÿ]", word)):
        return False
    return True


def get_valid_words(english_only: bool) -> List[str]:
    with open(FilePaths.ENGLISH) as f:
        words = f.readlines()
    if not english_only:
        with open(FilePaths.FRENCH) as f:
            words += f.readlines()
    return [word.rstrip("\n") for word in words if is_valid(word)]


def salt_password(password: str) -> [str, int]:
    position = random.randrange(len(password))
    digit = random.randrange(10)
    added_complexity = 10 * len(password)
    return f"{password[:position]}{digit}{password[position:]}", added_complexity


def get_entropy(length: int, dict_cardinal: int, added_complexity: int) -> int:
    return int(math.log(dict_cardinal ** length * added_complexity) / math.log(2))


def format_password_to_common_rules(password: str) -> str:
    return f"{password.capitalize()}0."


@click.command()
@click.option(
    "--length", "-l", default=6, help="Number of words used to create password."
)
@click.option("--salt", default=False, help="Add some entropy", is_flag=True)
@click.option(
    "--english_only", default=False, help="Use only english dictionary", is_flag=True
)
def generate_password(length: int, salt: bool, english_only: bool) -> [str, float]:
    valid_words = get_valid_words(english_only=english_only)
    new_password = ""
    password_length = 0
    while password_length < length:
        new_word = random.choice(valid_words)
        if is_valid(new_word):
            new_password = f"{new_word} {new_password}"
            password_length += 1
    added_complexity = 1
    if salt:
        new_password, added_complexity = salt_password(password=new_password)
    entropy = get_entropy(
        length=length, dict_cardinal=len(valid_words), added_complexity=added_complexity
    )
    new_password = format_password_to_common_rules(password=new_password)
    logger.info(
        f"{new_password} (Entropy: {entropy} - Dictionary: {len(valid_words)} words)"
    )
    return new_password, entropy


if __name__ == "__main__":
    generate_password()
