import math
import random
import re

import click
from loguru import logger

FILE_PATH = "/Users/plurielle/.french_common_words.txt"
MAX_SIZE_WORD = 9
MIN_SIZE_WORD = 2


def is_valid(word: str) -> bool:
    if len(word) >= MAX_SIZE_WORD:
        return False
    if len(word) <= MIN_SIZE_WORD:
        return False
    if bool(re.search(r"[À-ÿ]", word)):
        return False
    return True


@click.command()
@click.option('--length', '-l', default=6, help='Number of words used to create password.')
@click.option('--salt', default=False, help='Add some entropy', is_flag=True)
def generate_password(length: int, salt: bool = False) -> [str, float]:
    with open(FILE_PATH) as f:
        words = f.readlines()
    valid_words = [word.rstrip("\n") for word in words if is_valid(word)]
    logger.info(f"Creating password with {len(valid_words)} words")

    new_password = ""
    password_length = 0
    while password_length < length:
        new_word = random.choice(valid_words)
        if is_valid(new_word):
            new_password = f"{new_word} {new_password}"
            password_length += 1
    new_password = new_password.capitalize()
    salt_entropy = 1
    if salt:
        position = random.randrange(len(new_password))
        digit = random.randrange(10)
        new_password = f"{new_password[:position]}{digit}{new_password[position:]}"
        salt_entropy = 10 * len(new_password)
    new_password = f"{new_password.capitalize()}0."
    entropy = int(math.log(
        len(valid_words) ** length * salt_entropy
    ) / math.log(2))
    logger.info(f"{new_password} (entropy: {entropy})")
    return new_password, entropy


if __name__ == '__main__':
    generate_password()
