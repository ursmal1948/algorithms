import unittest
from algorithms.ciphers.caesar import CaesarCipher


class TestCaesarWithDefaultShift(unittest.TestCase):
    test_cases = [
        ('ABC', 'DEF'),
        ('XYZ', 'ABC'),
        ('GHI', 'JKL'),
        ('123!', '123!'),
        ('G4HI', 'J4KL')
    ]

    @classmethod
    def setUpClass(cls):
        cls.caesar_cipher = CaesarCipher()

    def test_encrypt(self):
        for case in TestCaesarWithDefaultShift.test_cases:
            with self.subTest(case=case):
                text, expected_encrypted_text = case
                encrypted_text = self.caesar_cipher.encrypt_text(text)
                self.assertEqual(encrypted_text, expected_encrypted_text)

    def test_decrypt(self):
        for case in TestCaesarWithDefaultShift.test_cases:
            with self.subTest(case=case):
                expected_decrypted_text, encrypted_text = case
                decrypted_text = self.caesar_cipher.decrypt_text(encrypted_text)
                self.assertEqual(decrypted_text, expected_decrypted_text)


class TestCaesarWithCustomShift(unittest.TestCase):
    test_cases = [
        ('ABC', 'ABC', 0),
        ('XYZ', 'YZA', 1),
        ('GHI', 'EFG', -2),
        ('123!', '123!', 10),
        ('G4HI', 'L4MN', 5)
    ]
    # def setUp(self): # PARAMETRYZACJA
    #     self.caesar_cipher = CaesarCipher(3)

    def test_encypt(self):
        for case in TestCaesarWithCustomShift.test_cases:
            with self.subTest(case=case):
                text, expected_encrypted_text, shift = case
                encrypted_text = CaesarCipher(shift).encrypt_text(text)
                assert encrypted_text == expected_encrypted_text

    def test_decrypt(self):
        for case in self.test_cases:
            with self.subTest(case=case):
                expected_decrypted_text, encrypted_text, shift = case
                decrypted_text = CaesarCipher(shift).decrypt_text(encrypted_text)
                assert decrypted_text == expected_decrypted_text
