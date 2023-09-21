import pytest
import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

S = requests.Session()

@pytest.fixture()
def user_login():
    result = S.post(url=data['url'], data={'username': data['login'], 'password': data['pswd']})
    response_json = result.json()
    token = response_json.get('token')
    return token


@pytest.fixture()
def get_description():
    return 'New_description_for_test_HW'

@pytest.fixture()
def post_title():
    return 'TestTitle' #постоянно меняется

#
# result = S.post(url=data['url'], data={'username': data['login'], 'password': data['pswd']})
# response_json = result.json()
# token = response_json.get('token')
# print(token)

