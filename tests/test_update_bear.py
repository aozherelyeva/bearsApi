from bear_api import update_bear, get_one_bear

BEAR_TYPE = "POLAR"
BEAR_NAME = "potapych"
BEAR_AGE = 5
new_bear_data = {"bear_type": f"{BEAR_TYPE}", "bear_name": f"{BEAR_NAME}", "bear_age": f"{BEAR_AGE}"}


def test_update_bear(bear_id):
    response = update_bear(bear_id, new_bear_data)
    assert response.status_code == 200, f"Status code is wrong, expected 200, got {response.status_code}"
    new_body = dict(get_one_bear(bear_id).text)
    assert new_body.get("bear_type") == f"{BEAR_TYPE}"
    assert new_body.get("bear_name") == f"{BEAR_NAME}"
    assert new_body.get("bear_age") == f"{BEAR_AGE}"
