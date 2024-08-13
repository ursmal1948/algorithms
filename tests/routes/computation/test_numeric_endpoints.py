import pytest


# todo bisection root
class TestNumericAlgorithmsEndpoints:

    def test_trapezoidal_integration_route(self, client, trapezoidal_integration_path):
        json_payload = {
            "function_body": "x - 3",
            "a": 3,
            "b": 8,
            "n": 200
        }

        response = client.post(trapezoidal_integration_path, json=json_payload)
        assert response.json["integration result"] == 12.5
        assert response.status_code == 200

    def test_trapezoidal_integration_route_with_invalid_json(self, client,
                                                             trapezoidal_integration_path):
        json_payload = {
            "a": 3,
            "b": 8,
            "n": 200
        }
        response = client.post(trapezoidal_integration_path, json=json_payload)
        assert "function_body' is a required property" in response.json['message']

    def test_rectangular_integration_route(self, client, rectangular_integration_path):
        json_payload = {
            "coefficients": [1, 1, -3, 4],
            "a": -2,
            "b": 2,
            "n": 50
        }
        response = client.post(rectangular_integration_path, json=json_payload)
        assert round(response.json["integration result"], 2) == 21.33
        assert response.status_code == 200

    def test_rectangular_integration_route_with_invalid_json(self, client,
                                                             rectangular_integration_path):
        json_payload = {
            "a": -2,
            "b": 2,
            "n": 50
        }
        response = client.post(rectangular_integration_path, json=json_payload)
        assert "coefficients' is a required property" in response.json['message']
