import bear_api

new_bear_data = {"bear_type": "POLAR", "bear_name": "potapych", "bear_age": "5"}


def test_update_bear(bear_id):
    response = bear_api.update_bear(bear_id, new_bear_data)
    assert response.status_code == 200, f"Status code is wrong, expected 200, got {response.status_code}"
    '''Вижу тут необходимость добавть get-запрос на мишку и проверить, что данные в теле ответа совпадают
    с обновленными согласно new_bear_data, но пока не успела разобраться, как это сделать.'''
