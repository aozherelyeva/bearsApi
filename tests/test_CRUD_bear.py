import json

import pytest
from jsonschema import validate

from bear_api import delete_all_bears, create_bear, get_one_bear, update_bear, get_bears_list, delete_one_bear

bear_data = {"bear_type": "BLACK", "bear_name": "mikhail", "bear_age": "1"}
new_bear_data = {"bear_type": "POLAR", "bear_name": "potapych", "bear_age": "5"}

schema_single = {
    "type": "object",
    "properties": {
        "bear_id": {"type": "number"},
        "bear_type": {"type": "string"},
        "bear_name": {"type": "string"},
        "bear_age": {"type": "number"},
    }
}


@pytest.mark.parametrize('path', ["/bear", "/bear/2"])
def test_crud_bears(path):
    bears = get_bears_list().response().text
    if bears == "[]":
        pass
    else:
        delete_all_bears()

    create_bear(bear_data)
    new_bear = int(create_bear(bear_data).text)
    assert create_bear(
        bear_data).status_code == 201, f"Status code is wrong, expected 201, got {create_bear(bear_data).status_code}"

    get_one_bear(new_bear)
    assert get_one_bear(
        new_bear).status_code == 200, f"Status code is wrong, expected 200, got {get_one_bear(new_bear).status_code}"
    body = json.loads(get_one_bear(new_bear).text)
    validate(instance=body, schema=schema_single)
    bear_info = dict(get_one_bear(new_bear).text)
    assert bear_info.get("bear_type") == "BLACK"
    assert bear_info.get("bear_name") == "mikhail"
    assert int(bear_info.get("bear_age")) == 1

    update_bear(new_bear, new_bear_data)
    assert update_bear(new_bear,
                       new_bear_data).status_code == 200, f"Status code is wrong, expected 200, " \
                                                          f"got {update_bear(new_bear, new_bear_data).status_code}"
    new_bear_info = dict(get_one_bear(new_bear).text)
    assert new_bear_info.get("bear_type") == "POLAR"
    assert new_bear_info.get("bear_name") == "potapych"
    assert int(new_bear_info.get("bear_age")) == 5

    delete_one_bear(new_bear)
    assert delete_one_bear(
        new_bear).status_code == 200, f"Status code is wrong, expected 200, got {delete_one_bear(new_bear).status_code}"

    get_bears_list()
    body = json.loads(get_bears_list().response.text)
    assert body == "[]"
