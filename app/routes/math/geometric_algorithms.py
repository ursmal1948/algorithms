from app.algohub.algorithms.math.geometric_algorithms import (
    Point,
    distance_between_points,
    are_points_collinear,
    is_triangle_valid,
    is_triangle_rectangular
)
from flask import Flask, jsonify, request, Blueprint, Response
from flask_restful import reqparse
from flask_json_schema import JsonSchema
from app.routes.schemas import (
    two_coordinates_list_schema,
    three_coordinates_list_schema,
    triangle_side_schema)
import logging

logging.basicConfig(level=logging.INFO)

schema = JsonSchema()
geometric_algorithms_blueprint = Blueprint(
    'geometric-algorithms',
    __name__,
    url_prefix='/api/algorithms/math/geometric-algorithms'
)


@geometric_algorithms_blueprint.route('/distance-between-points', methods=['POST'])
@schema.validate(two_coordinates_list_schema)
def handle_distance_between_points() -> Response:
    json_body = request.json
    point1_coord, point2_coord = json_body['point1'], json_body['point2']
    point1, point2 = Point.from_list(point1_coord), Point.from_list(point2_coord)
    points_distance = distance_between_points(point1, point2)
    return jsonify({'distance': points_distance})


@geometric_algorithms_blueprint.route('/collinearity', methods=['POST'])
@schema.validate(three_coordinates_list_schema)
def handle_collinearity() -> Response:
    json_body = request.json
    point1_coord = json_body['point1']
    point2_coord = json_body['point2']
    point3_cord = json_body['point3']
    point1, point2, point3, = (
        Point.from_list(point1_coord),
        Point.from_list(point2_coord),
        Point.from_list(point3_cord)
    )
    collinearity = are_points_collinear(point1, point2, point3)
    return jsonify({'collinearity': collinearity}), 200


@geometric_algorithms_blueprint.route('/valid-triangle', methods=['POST'])
@schema.validate(triangle_side_schema)
def handle_is_triangle_valid() -> Response:
    json_body = request.json
    s1, s2, s3 = json_body['side1'], json_body['side2'], json_body['side3']
    validity = is_triangle_valid(s1, s2, s3)
    return jsonify({'validity': validity}), 200


@geometric_algorithms_blueprint.route('/rectangular-triangle', methods=['POST'])
@schema.validate(triangle_side_schema)
def handle_is_triangle_rect() -> Response:
    json_body = request.json
    s1, s2, s3 = json_body['side1'], json_body['side2'], json_body['side3']
    rectangularity = is_triangle_rectangular(s1, s2, s3)
    return jsonify({'rectangularity': rectangularity}), 200


# todo stare podejscie. taki blad dostawalam. w ramach konwersji wyskakiwal blad.

#     @app.route('/valid-triangle', methods=['GET'])
#     def handle_is_triangle_valid():
#         s1, s2, s3 = int(request.args.get('a')), int(request.args.get('b')), int(request.args.get('c'))
# jak nie podalam
# {
#     "message": "int() argument must be a string, a bytes-like object or a real number, not 'NoneType'"
# }
#         validity = is_triangle_valid(s1, s2, s3)
#         return jsonify({f'Valid triangle with sides: {s1} {s2} {s3} ': validity})
