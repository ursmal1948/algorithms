from string import ascii_lowercase

# import json
import pytest
import requests
import logging

logging.basicConfig(level=logging.INFO)


class TestStringAnalysisEndpoints:

    @pytest.mark.parametrize('payload_arg, expected_result', [
        ('abcd', False),
        ('ABA', True),
        ('', False)

    ])
    def test_palindrome_route(self, client, payload_arg, expected_result, palindrome_path):
        json_payload = {
            'text': payload_arg,
        }
        response = client.post(palindrome_path, json=json_payload)

        if response.status_code == 200:
            assert response.json['palindrome'] == expected_result
        else:
            assert response.status_code == 500
            assert (response.json['message'] ==
                    "('Error validating against schema', [<ValidationError: \"'' should be non-empty\">])"
                    )

    @pytest.mark.parametrize('potential_pangram, expected_result', [
        (ascii_lowercase, True),
        ('AB', False),
        ('', False)
    ])
    def test_pangram_route(self, client, potential_pangram, expected_result, pangram_path):
        json_payload = {
            'text': potential_pangram
        }
        response = client.post(pangram_path, json=json_payload)
        if response.status_code == 500:
            assert (response.json['message'] ==
                    "('Error validating against schema', [<ValidationError: \"'' should be non-empty\">])"
                    )
        else:
            assert response.json['pangram'] == expected_result
            assert response.status_code == 200

    @pytest.mark.parametrize('payload_arg1, payload_arg2, expected_result', [
        ['abc', 'cba', True],
        ['ab', 'bd', False]
    ])
    def test_anagrams_route(self, client, payload_arg1, payload_arg2, expected_result, anagrams_path):
        json_payload = {
            'text1': payload_arg1,
            'text2': payload_arg2,
        }
        response = client.post(anagrams_path, json=json_payload)
        assert response.status_code == 200
        assert response.json['anagrams'] == expected_result
