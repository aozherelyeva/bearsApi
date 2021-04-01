import json

import bear_api

bear_data = {"bear_type": "BLACK", "bear_name": "mikhail", "bear_age": "1"}


def test_create_bear():
    response = bear_api.create_bear(bear_data)
    assert response.status_code == 201, f"Status code is wrong, expected 200, got {response.status_code}"
    body = json.loads(response.text)
    '''так как мы ждем в ответе ID созданного мишки'''
    assert len(body) > 0
    '''Можно также добавить здесь get-запрос на созданного мишку и проверить, что данные в его теле совпадают
    с переданными в bear_data, но я не успела разобраться с тем, как именно это сделать. Оставляю в Todo на будущее.'''
