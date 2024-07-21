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
