from string import ascii_uppercase
from dataclasses import dataclass
from abc import ABC, abstractmethod


class _VigenereGenerator(ABC):
    """
    Abstract class for generating a Vigenere square.
    """

    @abstractmethod
    def generate_vigenere_square(self, n: int = 26) -> list[list[str]]:
        """
        :param n: int (default is 26) number of rows in the Vigenere square
        :return list[list[str]]:  a list of lists representing the Vigenere square
        """
        pass


class _VigenereSquareGenerator(_VigenereGenerator):
    """
    A derived class of _VigenereGenerator class for generating a Vigenere square, which is a tabular
     arrangement of alphabets used in the Vigenere cipher for encryption and decryption
    """

    def generate_vigenere_square(self, n: int = 26) -> list[list[str]]:
        """
        Generates a vigenere square of size 'n' (default is 26)
         as a list of lists, where each sublist represents a row of the Vigenere square
        :param n: int (default is 26) number of rows in the Vigenere square
        :return list[list[str]]:  a list of lists representing the Vigenere square
        """
        return [(list(ascii_uppercase[i:] + ascii_uppercase[:i])) for i in range(n)]


@dataclass
class VigenereCipher:
    """
    A class for Vigenere Cipher encryption and decryption

    Attributes:
        key: str
         A key used for encryption and decryption. It determines the row in the Vigenere square
         to use for each character
        vigenere_generator: _VigenereGenerator
         An instance of the Vigenere square generator
    """
    key: str = 'KEY'
    vigenere_generator: _VigenereGenerator = _VigenereSquareGenerator()

    def encrypt(self, text: str) -> str:
        """
        Encrypts the given text using the Vigenere cipher and provided key
        :param text: str text to be encrypted
        :return str: the encrypted text
        """
        cleaned_text = [c for c in text if c.isalpha()]
        vigenere_square = self.vigenere_generator.generate_vigenere_square()
        chars = []
        for i in range(len(cleaned_text)):
            current_key_char = self.key[i % len(self.key)]
            row = ord(current_key_char) - ord('A')
            column = vigenere_square[0].index(cleaned_text[i])
            encrypted_char = vigenere_square[row][column]
            chars.append(encrypted_char)
        return ''.join(chars)

    def decrypt(self, encrypted_text: str) -> str:
        """
        Decrypts the given encrypted text using the Vigenere cipher and provided key
        :param encrypted_text: str text to be decrypted
        :return str: the decrypted text
        """
        cleaned_text = [c for c in encrypted_text if c.isalpha()]
        vigenere_square = self.vigenere_generator.generate_vigenere_square()
        chars = []

        for i in range(len(cleaned_text)):
            current_key_char = self.key[i % len(self.key)]
            row = ord(current_key_char) - ord('A')
            column = vigenere_square[row].index(cleaned_text[i])
            decrypted_char = vigenere_square[0][column]
            chars.append(decrypted_char)

        return ''.join(chars)
