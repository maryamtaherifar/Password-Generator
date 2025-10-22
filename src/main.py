import random
import string
from abc import ABC, abstractmethod
from typing import Iterable

import nltk


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = True, include_symbols: bool = False, require_all: bool = True):
        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols
        self.characters = string.ascii_letters
        self.require_all = require_all

        if self.include_numbers:
            self.characters += string.digits
        if self.include_symbols:
            self.characters += '!@#$%^&*-_'

    def generate(self):
        characters = []
        if self.require_all:
            characters.append(random.choice(string.ascii_lowercase))
            characters.append(random.choice(string.ascii_uppercase))
            if self.include_numbers:
                characters.append(random.choice(string.digits))
            if self.include_symbols:
                characters.append(random.choice('!@#$%^&*-_'))
        characters += [random.choice(self.characters) for _ in range(self.length - len(characters))]
        random.shuffle(characters)
        password = ''.join(characters)

        return password


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, number_of_words: int = 4, seperator: str = '-', capitalize: bool = False, random_lower_upper: bool = False, vocabulary: Iterable[str] = None):
        self.number_of_words = number_of_words
        self.seperator = seperator
        self.capitalize = capitalize
        self.random_lower_upper = random_lower_upper
        self.vocabulary = vocabulary or nltk.corpus.words.words()

    def generate(self):
        words = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]
        if self.capitalize:
            words = [word.capitalize() for word in words]

        if self.random_lower_upper:
            words = [word.upper() if random.choice([True, False]) else word.lower() for word in words]

        return self.seperator.join(words)


class PinGenerator(PasswordGenerator):
    def __init__(self, length:int=8):
        self.length = length

    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


if __name__ == '__main__':
    pin_pass = PinGenerator()
    random_pass = RandomPasswordGenerator(include_symbols= True)
    memorable_pass = MemorablePasswordGenerator(random_lower_upper= True)
    print(f'Pin password: {pin_pass.generate()}\nRandom password: {random_pass.generate()}\nMemorable password: {memorable_pass.generate()}')
