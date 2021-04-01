from bear_api import update_bear, get_one_bear

new_bear_data = {"bear_type": "POLAR", "bear_name": "potapych", "bear_age": 5}


def test_update_bear(bear_id):
    response = update_bear(bear_id, new_bear_data)
    assert response.status_code == 200, f"Status code is wrong, expected 200, got {response.status_code}"
    new_body = dict(get_one_bear(bear_id).text)
    assert new_body.get("bear_type") == "POLAR"
    assert new_body.get("bear_name") == "potapych"
    assert int(new_body.get("bear_age")) == 5
