import pytest


class TestFunctionAlgorithmsEndpoints:
    def test_quadratic_roots_route(self, client, quadratic_roots_path):
        json_body = {
            "a": 1,
            "b": 10,
            "c": 25
        }
        response = client.post(quadratic_roots_path, json=json_body)
        assert response.status_code == 200
        assert response.json['result'] == [-5.0, -5.0]

    def test_quadratic_roots_route_when_a_coeff_equals_0(self, client, quadratic_roots_path):
        json_body = {
            "a": 0
        }
        response = client.post(quadratic_roots_path, json=json_body)
        assert response.status_code == 500
        assert response.json['message'] == 'Coefficient a must be a non-zero for a quadratic equation'

    def test_quadratic_roots_route_when_invalid_json(self, client, quadratic_roots_path):
        json_body = {}
        response = client.post(quadratic_roots_path, json=json_body)
        assert response.status_code == 500
        assert "'a' is a required property" in response.json['message']

    def test_horner_route(self, client, horner_path):
        json_body = {
            "coefficients": [1, 3, 13],
            "value": 5
        }
        response = client.post(horner_path, json=json_body)
        assert response.status_code == 200
        assert response.json['result'] == 53

    def test_horner_route_when_invalid_json(self, client, horner_path):
        json_body = {}
        response = client.post(horner_path, json=json_body)
        assert response.status_code == 500
        assert "'coefficients' is a required property" in response.json['message']
        assert "'value' is a required property" in response.json['message']
