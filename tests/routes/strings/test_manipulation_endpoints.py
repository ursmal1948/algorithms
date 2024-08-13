import pytest


class TestStringManipulationEndpoints:

    def test_custom_join_route_with_default_separator(self, client, custom_join_path):
        json_payload = {'text': 'ABC'}
        response = client.post(custom_join_path, json=json_payload)
        assert response.status_code == 200
        assert response.json['joined'] == 'A-B-C'

    def test_custom_join_route_with_custom_separator(self, client, custom_join_path):
        json_payload = {'text': 'ABC', 'separator': '*'}
        response = client.post(custom_join_path, json=json_payload)
        assert response.status_code == 200
        assert response.json['joined'] == 'A*B*C'

    @pytest.mark.parametrize('text, case, expected_result', [
        ('abc', 'upper', 'ABC'),
        ('DEF', 'lower', 'def')
    ])
    def test_lower_upper_transformation_route(self, client, text, case, expected_result, transformation_path):
        json_payload = {'text': text, 'case': case}
        response = client.post(transformation_path, json=json_payload)
        assert response.status_code == 200
        assert response.json['transformed'] == expected_result

    def test_transformation_route_invalid_case(self, client, transformation_path):
        json_payload = {'text': 'ABC', 'case': 'invalid_case'}
        response = client.post(transformation_path, json=json_payload)
        assert response.status_code == 400
        assert response.json['message'] == 'invalid case'

    def test_transformation_route_with_empty_string(self, client, transformation_path):
        json_payload = {'text': '', 'case': 'lower'}
        response = client.post(transformation_path, json=json_payload)
        assert response.status_code == 500
        assert (response.json['message'] ==
                "('Error validating against schema', [<ValidationError: \"'' should be non-empty\">])"
                )

    def test_compress_route(self, client, compress_path):
        json_payload = {'text': 'ABBBAC'}
        response = client.post(compress_path, json=json_payload)
        assert response.status_code == 200
        assert response.json['compressed'] == 'A2B3C1'

    def test_compress_route_with_empty_string(self, client, compress_path):
        json_payload = {'text': ''}
        response = client.post(compress_path, json=json_payload)
        assert response.status_code == 500
        assert (response.json['message'] ==
                "('Error validating against schema', [<ValidationError: \"'' should be non-empty\">])"
                )

    def test_reverse_route(self, client, reverse_path):
        json_payload = {'text': 'ABC'}
        response = client.post(reverse_path, json=json_payload)
        assert response.status_code == 200
        assert response.json['reversed'] == 'CBA'
