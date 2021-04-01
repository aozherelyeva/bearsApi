import json

import bear_api
from jsonschema import validate

schema_all = {
    "type": "array",
    "properties": {
        "bear_id": {"type": "number"},
        "bear_type": {"type": "string"},
        "bear_name": {"type": "string"},
        "bear_age": {"type": "number"},
    }
}
schema_single = {
    "type": "object",
    "properties": {
        "bear_id": {"type": "number"},
        "bear_type": {"type": "string"},
        "bear_name": {"type": "string"},
        "bear_age": {"type": "number"},
    }
}


def test_get_bears_list():
    response = bear_api.get_bears_list()
    assert response.status_code == 200, f"Status code is wrong, expected 200, got {response.status_code}"
    body = json.loads(response.text)
    validate(instance=body, schema=schema_all)


def test_get_one_bear(bear_id):
    response = bear_api.get_one_bear(bear_id)
    assert response.status_code == 200, f"Status code is wrong, expected 200, got {response.status_code}"
    body = json.loads(response.text)
    validate(instance=body, schema=schema_single)
