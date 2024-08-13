import pytest


@pytest.fixture(params=[[3, 6], [0, 1], [4, 24]])
def factorial_fixture(request):
    return request.param


class TestArithmeticAlgorithmsEndpoints:
    @staticmethod
    def _factorial_path(method: str, number: int) -> str:
        return f'/api/algorithms/computation/arithmetic/factorial/{method}/{number}'

    def test_factorial_routes(self, client, factorial_fixture):
        number, result = factorial_fixture
        iterative_factorial_path = TestArithmeticAlgorithmsEndpoints._factorial_path('iterative', number)
        recursive_factorial_path = TestArithmeticAlgorithmsEndpoints._factorial_path('recursive', number)

        response_1 = client.get(iterative_factorial_path)
        response_2 = client.get(recursive_factorial_path)
        assert response_1.status_code == 200
        assert response_1.json['factorial'] == result
        assert response_1.json['method'] == 'iterative'

        assert response_2.status_code == 200
        assert response_2.json['factorial'] == result
        assert response_2.json['method'] == 'recursive'

    def test_factorial_route_invalid_method(self, client):
        invalid_method = TestArithmeticAlgorithmsEndpoints._factorial_path('invalid', 5)
        response = client.get(invalid_method)
        assert response.status_code == 400
        assert response.json['message'] == 'Wrong factorial method'

    def test_binary_search_route(self, client, binary_search_path):
        json_payload = {'numbers': [10, 20, 30, 40], 'target': 20}
        response = client.post(binary_search_path, json=json_payload)
        assert response.status_code == 200
        assert response.json['result'] == 1

    def test_binary_search_route_number_not_found(self, client, binary_search_path):
        json_payload = {'numbers': [10, 20, 30, 40], 'target': 100}
        response = client.post(binary_search_path, json=json_payload)
        assert response.status_code == 400
        assert response.json['message'] == 'Number not found'
