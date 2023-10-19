eTraP_CLASS_TO_IDX_MAPPING = {
    'pedestrian': 0,
    'car': 1,
    'bicycle': 2,
    'bus': 3,
    'bike': 4,
    'truck': 5,
    'tram': 6,
    'wheelchair': 7
}


def value_to_key(dictionary, val):
    for key, value in dictionary.items():
        if value == val:
            return key
    return None