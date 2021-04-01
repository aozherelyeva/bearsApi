from bear_api import delete_one_bear, delete_all_bears


def test_delete_all_bears():
    response = delete_all_bears()
    assert response.status_code == 200, f"Status code is wrong, expected 200, got {response.status_code}"


def test_delete_one_bear(bear_id):
    response = delete_one_bear(bear_id)
    assert response.status_code == 200, f"Status code is wrong, expected 200, got {response.status_code}"
