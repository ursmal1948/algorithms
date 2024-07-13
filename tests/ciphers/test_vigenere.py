import unittest
from app.algohub.algorithms.ciphers.vigenere import VigenereCipher


class TestVigenereWithDefaultKey2(unittest.TestCase):
    test_cases = [
        ('KAYAK', 'UEWKO'),
        ('GARDEN', 'QEPNIL'),
        ('ABC', 'KFA'),
        ('A', 'K'),
        ('UNIVERSITY', 'ERGFIPCMRI')
    ]

    @classmethod
    def setUpClass(cls):
        cls.vigenere_cipher = VigenereCipher()

    def test_encrypt(self):
        for test_case in TestVigenereWithDefaultKey2.test_cases:
            with self.subTest(test_case=test_case):
                plain_text, expected_encrypted_text = test_case
                encrypted_text = self.vigenere_cipher.encrypt(plain_text)
                self.assertEqual(encrypted_text, expected_encrypted_text)

    def test_decrypt(self):
        for test_case in TestVigenereWithDefaultKey2.test_cases:
            with self.subTest(test_case=test_case):
                expected_decrypted_text, encrypted_text = test_case
                decrypted_text = self.vigenere_cipher.decrypt(encrypted_text)
                self.assertEqual(decrypted_text, expected_decrypted_text)


class TestVigenereWithCustomKey2(unittest.TestCase):
    test_cases = [
        ('KAYAK', 'SON', 'COLSY'),
        ('TEXT', 'WATERFALL', 'PEQX'),
        ('BCD', 'BCD', 'CEG'),
        ('S', 'MUD', 'E'),
        ('UNIVERSITY', 'LEAF', 'FRIAPVSNEC')
    ]

    def test_encrypt(self):
        for test_case in TestVigenereWithCustomKey2.test_cases:
            with self.subTest(test_case=test_case):
                plain_text, key, enxpected_encrypted_text = test_case
                vigenere_cipher = VigenereCipher(key)
                encrypted_text = vigenere_cipher.encrypt(plain_text)
                self.assertEqual(encrypted_text, enxpected_encrypted_text)

    def test_decrypt(self):
        for test_case in TestVigenereWithCustomKey2.test_cases:
            with self.subTest(test_case=test_case):
                expected_decrypted_text, key, encrypted_text = test_case
                vigenere_cipher = VigenereCipher(key)
                decrypted_text = vigenere_cipher.decrypt(encrypted_text)
                self.assertEqual(decrypted_text, expected_decrypted_text)
