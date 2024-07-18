from app.algohub.algorithms.math.geometric_algorithms import (
    Point,
    distance_between_points,
    are_points_collinear,
    is_triangle_valid,
    is_triangle_rectangular
)
from flask import Flask, jsonify, request
from flask_restful import reqparse

import logging

logging.basicConfig(level=logging.INFO)


def configure_geometric_algorithms(app: Flask) -> None:
    @app.route('/distance-between-points', methods=['GET'])
    def calculate_distance_between_points():
        parser = reqparse.RequestParser()
        parser.add_argument('point1', type=list, location='json', help='Point 1 coordinates', required=True)
        parser.add_argument('point2', type=list, location='json', help='Point 2 coordinates', required=True)
        request_data = parser.parse_args()
        point1_coordinates = request_data['point1']
        point2_coordinates = request_data['point2']
        point1, point2 = Point.from_list(point1_coordinates), Point.from_list(point2_coordinates)
        points_distance = distance_between_points(point1, point2)
        return jsonify({'Distance between points': points_distance}), 200

    @app.route('/collinearity', methods=['GET'])
    def handle_are_points_collinear():
        parser = reqparse.RequestParser()
        parser.add_argument('point1', type=list, location='json', help='Point 1 coordinates', required=True)
        parser.add_argument('point2', type=list, location='json', help='Point 2 coordinates', required=True)
        parser.add_argument('point3', type=list, location='json', help='Point 3 coordinates', required=True)

        request_data = parser.parse_args()
        point1_coordinates = request_data['point1']
        point2_coordinates = request_data['point2']
        point3_coordinates = request_data['point3']
        point1, point2, point3 = (Point.from_list(point1_coordinates),
                                  Point.from_list(point2_coordinates),
                                  Point.from_list(point3_coordinates))
        collinearity = are_points_collinear(point1, point2, point3)

        return jsonify({'Collinearity between points': collinearity})

    @app.route('/valid-triangle', methods=['GET'])
    def handle_is_triangle_valid():
        s1, s2, s3 = int(request.args.get('a')), int(request.args.get('b')), int(request.args.get('c'))
        validity = is_triangle_valid(s1, s2, s3)
        return jsonify({f'Valid triangle with sides: {s1} {s2} {s3} ': validity})

    @app.route('/rectangular-triangle', methods=['GET'])
    def handle_is_triangle_rectangular():
        parser = reqparse.RequestParser()
        parser.add_argument('side1', type=int)
        parser.add_argument('side2', type=int)
        parser.add_argument('side3', type=int)
        request_data = parser.parse_args()
        logging.info(request_data)
        s1, s2, s3 = request_data['side1'], request_data['side2'], request_data['side3']
        rectangularity = is_triangle_rectangular(s1, s2, s3)
        return {'Triangle rectangularity': rectangularity}
