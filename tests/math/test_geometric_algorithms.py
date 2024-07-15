import pytest

from app.algohub.algorithms.math.geometric_algorithms import (
    Point,
    distance_between_points,
    are_points_collinear,
    is_triangle_valid,
    is_triangle_rectangular,
)


class TestPointsGeometryTester:
    @pytest.mark.parametrize('p1, p2, expected_distance', [
        (Point(0, 0), Point(4, 0), 4.0),
        (Point(0, 0), Point(3, 4), 5.0),
        (Point(-2, -3), Point(1, 1), 5.0),
        (Point(1.5, 2.5), Point(3.7, 4.9), 3.26)
    ])
    def test_calculate_distance_between_points(self, p1, p2, expected_distance):
        distance = distance_between_points(p1, p2)
        assert distance == expected_distance

    @pytest.mark.parametrize('p1, p2,p3, expected_collinearity', [
        (Point(0, 0), Point(1, 1), Point(2, 2), True),
        (Point(0, 0), Point(1, 1), Point(2, 3), False),
        (Point(-3, -3), Point(-2, -2), Point(-1, -1), True),
        (Point(-3, 0), Point(-2, -2), Point(-1, -1), False),
        (Point(1.5, 4), Point(3.5, 8), Point(5.25, 11.5), True),
        (Point(100, 210), Point(300, 610), Point(500, 1010), True)

    ])
    def test_are_points_collinear(self, p1, p2, p3, expected_collinearity):
        collinearity = are_points_collinear(p1, p2, p3)
        assert collinearity == expected_collinearity


class TestTriangleProperties:
    @pytest.mark.parametrize('s1, s2, s3, expected_result', [
        (2, 3, 10, False),
        (1, 1, 1, True),
        (3, 4, 7, False),
        (5, 8, 10, True),
        (3.5, 4.5, 7.5, True),
    ])
    def test_is_triangle_valid(self, s1, s2, s3, expected_result):
        validity = is_triangle_valid(s1, s2, s3)
        assert validity == expected_result

    @pytest.mark.parametrize('s1, s2, s3, expected_result', [
        (1, 1, 1, False),
        (3, 4, 5, True),
        (3, 4, 8, False),
        (40, 30, 50, True),
    ])
    def test_is_triangle_rectangular(self, s1, s2, s3, expected_result):
        is_rectangular = is_triangle_rectangular(s1, s2, s3)
        assert is_rectangular == expected_result


