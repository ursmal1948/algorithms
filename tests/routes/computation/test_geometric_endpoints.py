import pytest


class TestGeometricAlgorithmsEndpoints:
    def test_distance_between_points_route(self, client, points_distance_path):
        json_body = {
            "point1": [0, 0],
            "point2": [3, 4],
        }
        response = client.post(points_distance_path, json=json_body)
        assert response.status_code == 200
        assert response.json['distance'] == 5.0

    def test_distance_between_points_route_with_invalid_coordinates(self, client, points_distance_path):
        json_body = {
            "point1": [0, 0],
            "point2": [3],
        }
        response = client.post(points_distance_path, json=json_body)
        assert response.status_code == 500
        assert response.json['message'] == "2 coordinates must be provided for point"

    def test_collinearity_points_route(self, client, points_collinearity_path):
        json_body = {
            "point1": [1, 5],
            "point2": [2, 10],
            "point3": [3, 15],
        }
        response = client.post(points_collinearity_path, json=json_body)
        assert response.status_code == 200
        assert response.json['collinearity']

    def test_collinearity_points_route_no_collinearity(self, client, points_collinearity_path):
        json_body = {
            "point1": [1, 5],
            "point2": [2, 33],
            "point3": [4, 0],
        }
        response = client.post(points_collinearity_path, json=json_body)
        assert response.status_code == 200
        assert not response.json['collinearity']

    def test_collinearity_points_route_with_invalid_coordinates(self, client, points_collinearity_path):
        json_body = {
            "point1": [1, 5],
            "point2": [2, 33],
            "point3": [4]
        }
        response = client.post(points_collinearity_path, json=json_body)
        assert response.status_code == 500
        assert response.json['message'] == "2 coordinates must be provided for point"

    def test_valid_triangle_route(self, client, valid_triangle_path):
        json_body = {
            "side1": 3,
            "side2": 4,
            "side3": 6,
        }
        response = client.post(valid_triangle_path, json=json_body)
        assert response.status_code == 200

    def test_valid_triangle_route_with_invalid_triangle_scenario(self, client, valid_triangle_path):
        json_body = {
            "side1": 3,
            "side2": 4,
            "side3": 64,
        }
        response = client.post(valid_triangle_path, json=json_body)
        assert response.status_code == 200
        assert not response.json['validity']

    def test_rectangular_triangle_route(self, client, rectangular_triangle_path):
        json_body = {
            "side1": 6,
            "side2": 8,
            "side3": 10
        }
        response = client.post(rectangular_triangle_path, json=json_body)
        assert response.status_code == 200
        assert response.json['rectangularity']

    def test_rectangular_triangle_route_not_rectangular_scenario(self, client, rectangular_triangle_path):
        json_body = {
            "side1": 6,
            "side2": 8,
            "side3": 12
        }
        response = client.post(rectangular_triangle_path, json=json_body)
        assert response.status_code == 200
        assert not response.json['rectangularity']
