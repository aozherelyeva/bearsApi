import bear_api


def test_delete_all_bears():
    response = bear_api.delete_all_bears()
    assert response.status_code == 200, f"Status code is wrong, expected 200, got {response.status_code}"


def test_delete_one_bear(bear_id):
    response = bear_api.delete_one_bear(bear_id)
    assert response.status_code == 200, f"Status code is wrong, expected 200, got {response.status_code}"
