from bear_api import create_bear, get_one_bear

bear_data = {"bear_type": "BLACK", "bear_name": "mikhail", "bear_age": 1}


def test_create_bear():
    response = create_bear(bear_data)
    assert response.status_code == 201, f"Status code is wrong, expected 200, got {response.status_code}"
    bear_id = int(response.text)
    bear_body = dict(get_one_bear(bear_id).text)
    assert bear_body.get("bear_type") == "BLACK"
    assert bear_body.get("bear_name") == "mikhail"
    assert int(bear_body.get("bear_age")) == 1
