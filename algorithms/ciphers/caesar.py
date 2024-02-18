from dataclasses import dataclass
from typing import ClassVar
from string import ascii_uppercase


@dataclass
class CaesarCipher:
    """
    A class for implementing the Caesar cipher, a simple substitution cipher where each letter in the plaintext
    is shifted a certain number of places down or up the alphabet

    Attributes:
        sequence:str
         A sequence of characters representing the alphabet. Default is the ASCII uppercase characters
        shift: int
         The number of positions each letter is shifted. Default is 3
    """
    sequence: ClassVar[str] = ascii_uppercase
    shift: int = 3

    def _encrypt_char(self, char: str) -> str:
        """
        Encrypts a single character using the Caesar cipher
        :param char: str, the character to be encrypted
        :return str: the encrypted character
        """
        if char.isalpha() and char.isupper():
            return self.sequence[(self.sequence.index(char) + self.shift) % 26]
        return char

    def _decrypt_char(self, char: str) -> str:
        """
        Decrypts a single character using the Caesar cipher
        :param char: str, the character to be decrypted
        :return str: the decrypted character
        """
        if char.isalpha() and char.isupper():
            return self.sequence[(self.sequence.index(char) - self.shift) % 26]
        return char

    def encrypt_text(self, text: str) -> str:
        """
        Encrypts a given text using the Caesar cipher
        :param text: str, the text to be encrypted
        :return str: the encrypted text
        """
        return ''.join([self._encrypt_char(c) for c in text])

    def decrypt_text(self, encrypted_text: str) -> str:
        """
         Decrypts a given encrypted text using the Caesar cipher
        :param encrypted_text: str, the encrypted text to be decrypted
        :return str: the decrypted text
        """
        return ''.join([self._decrypt_char(c) for c in encrypted_text])
