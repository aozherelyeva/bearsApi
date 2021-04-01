from bear_api import create_bear, get_one_bear

BEAR_TYPE = "BLACK"
BEAR_NAME = "mikhail"
BEAR_AGE = 1
bear_data = {"bear_type": f"{BEAR_TYPE}", "bear_name": f"{BEAR_NAME}", "bear_age": f"{BEAR_AGE}"}


def test_create_bear():
    response = create_bear(bear_data)
    assert response.status_code == 201, f"Status code is wrong, expected 200, got {response.status_code}"
    bear_id = int(response.text)
    bear_body = dict(get_one_bear(bear_id).text)
    assert bear_body.get("bear_type") == f"{BEAR_TYPE}"
    assert bear_body.get("bear_name") == f"{BEAR_NAME}"
    assert bear_body.get("bear_age") == f"{BEAR_AGE}"
