text_schema = {
    "type": "object",
    "properties": {
        "text": {"type": "string"}
    },
    "required": ["text"]
}

anagrams_schema = {
    "type": "object",
    "properties": {
        "text1": {"type": "string"},
        "text2": {"type": "string"},
    },
    "required": ["text1", "text2"]
}
text_and_separator_schema = {
    "type": "object",
    "properties": {
        "text": {"type": "string"},
        "separator": {"type": "string"}
    },
    "required": ["text"]
}

text_and_case_schema = {
    "type": "object",
    "properties": {
        "text": {"type": "string"},
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
        "text": {"type": "string"},
        "shift": {"type": "integer"}
    },
    "required": ["text"]
}

vigenere_schema = {
    "type": "object",
    "properties": {
        "text": {"type": "string"},
        "key": {"type": "string"}
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
