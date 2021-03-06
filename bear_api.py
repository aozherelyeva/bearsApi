import requests

base_url = "http://localhost:80"
path = "/bear"


def get_bears_list() -> requests.Response:
    return requests.get(base_url + path)


def get_one_bear(bear_id) -> requests.Response:
    return requests.get(base_url + path + "/" + bear_id)


def create_bear(bear_data) -> requests.Response:
    return requests.post(base_url + path, data=bear_data)


def delete_all_bears() -> requests.Response:
    return requests.delete(base_url + path)


def delete_one_bear(bear_id) -> requests.Response:
    return requests.delete(base_url + path + "/" + bear_id)


def update_bear(bear_id, new_bear_data) -> requests.Response:
    return requests.put(base_url + path + "/" + bear_id, data=new_bear_data)
