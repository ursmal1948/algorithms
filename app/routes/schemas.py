text_schema = {
    "type": "object",
    "properties": {
        "text": {
            "type": "string",
            "minLength": 1
        }
    },
    "required": ["text"]
}

anagrams_schema = {
    "type": "object",
    "properties": {
        "text1": {"type": "string", "minLength": 1},
        "text2": {"type": "string", "minLength": 1},
    },
    "required": ["text1", "text2"]
}
text_and_separator_schema = {
    "type": "object",
    "properties": {
        "text": {"type": "string", "minLength": 1},
        "separator": {"type": "string"}
    },
    "required": ["text"]
}

text_and_case_schema = {
    "type": "object",
    "properties": {
        "text": {"type": "string", "minLength": 1},
        "case": {"type": "string"}
    },
    "required": ["text"]
}

range_schema = {
    "type": "object",
    "properties": {
        "r_start": {"type": "integer"},
        "r_end": {"type": "integer"}
    },
    "required": ["r_start", "r_end"]
}

numbers_list_schema = {
    "type": "object",
    "properties": {
        "numbers": {"type": "array", "items": {"type": "integer"}}
    },
    "required": ["numbers"]
}
caesar_schema = {
    "type": "object",
    "properties": {
        "text": {"type": "string", "minLength": 1},
        "shift": {"type": "integer"}
    },
    "required": ["text"]
}

vigenere_schema = {
    "type": "object",
    "properties": {
        "text": {"type": "string", "minLength": 1},
        "key": {"type": "string", "minLength": 1}
    },
    "required": ["text"]
}

morse_decryption_schema = {
    "type": "object",
    "properties": {
        "text": {"type": "string", "pattern": r'^[\\|.-]+$'}
    },
    "required": ["text"]
}
two_coordinates_list_schema = {
    "type": "object",
    "properties": {
        "point1": {"type": "array", "items": {"type": "number"}},
        "point2": {"type": "array", "items": {"type": "number"}}
    },
    "required": ["point1", "point2"]
}
three_coordinates_list_schema = {
    "type": "object",
    "properties": {
        "point1": {"type": "array", "items": {"type": "number"}},
        "point2": {"type": "array", "items": {"type": "number"}},
        "point3": {"type": "array", "items": {"type": "number"}}
    },
    "required": ["point1", "point2", "point3"]
}

triangle_side_schema = {
    "type": "object",
    "properties": {
        "side1": {"type": "number", "minimum": 0},
        "side2": {"type": "number", "minimum": 0},
        "side3": {"type": "number", "minimum": 0},
    },
    "required": ["side1", "side2", "side3"]
}

binary_search_schema = {
    "type": "object",
    "properties": {
        "numbers": {"type": "array", "items": {"type": "integer"}},
        "target": {"type": "integer"}
    },
    "required": ["numbers", "target"]
}

quadratic_equation_coefficiets_schema = {
    "type": "object",
    "properties": {
        "a": {"type": "number"},
        "b": {"type": "number"},
        "c": {"type": "number"},

    },
    "required": ["a"]
}
horner_schema = {
    "type": "object",
    "properties": {
        "coefficients": {"type": "array", "items": {"type": "number"}},
        "value": {"type": "number"}
    },
    "required": ["coefficients", "value"]
}
eratosthenes_schema = {
    "type": "object",
    "properties": {
        "sieve_upper_limit": {"type": "integer"},
        "looked_number": {"type": "integer"},
    },
    "required": ["sieve_upper_limit", "looked_number"]
}

bisection_root_schema = {
    "type": "object",
    "properties": {
        "coefficients": {"type": "array", "items": {"type": "number"}},
        "a": {"type": "number"},
        "b": {"type": "number"},
        "function_body": {"type": "string"}
    },
    "required": ["a", "b", "function_body"]
}
rectangular_integration_schema = {
    "type": "object",
    "properties": {
        "coefficients": {"type": "array", "items": {"type": "number"}},
        "a": {"type": "number"},
        "b": {"type": "number"},
        "n": {"type": "number"},
    },
    "required": ["coefficients", "a", "b", "n"]
}

trapezoidal_integration_schema = {
    "type": "object",
    "properties": {
        "function_body": {"type": "string"},
        "a": {"type": "number"},
        "b": {"type": "number"},
        "n": {"type": "number"},
    },
    "required": ["function_body", "a", "b", "n"]
}
