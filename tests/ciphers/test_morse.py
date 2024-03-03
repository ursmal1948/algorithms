import pytest
from algohub.algorithms.ciphers.morse import MorseCode


class TestMorse:

    @pytest.fixture(params=[
        ('SOMETHING', '...|---|--|.|-|....|..|-.|--.'),
        ('ABCDE12345', '.-|-...|-.-.|-..|.|.----|..---|...--|....-|.....'),
        ('A', '.-'),
        ('(?GHI.)', '-.--.|..--..|--.|....|..|.-.-.-|-.--.-')
    ])
    def morse_encoded_text(self, request):
        return request.param

    def test_encrypt(self, morse_encoded_text):
        text, expected_morse_encoding = morse_encoded_text
        morse_cipher = MorseCode()
        morse_encoding = morse_cipher.encrypt(text)
        assert morse_encoding == expected_morse_encoding

    def test_decrypt(self, morse_encoded_text):
        expected_decoded_text, morse_encoding = morse_encoded_text
        morse_cipher = MorseCode()
        decoded_text = morse_cipher.decrypt(morse_encoding)
        assert decoded_text == expected_decoded_text
