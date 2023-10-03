from http import HTTPStatus
from api.questions_api import api

def test_2_status():
    res = api.list_users()

    assert res.status_code == HTTPStatus.OK
    # Assert.validate_schema(res.json()) или res.text


def test_not_found():
    res = api.single_user_not_found()

    assert res.status_code == HTTPStatus.NOT_FOUND
    # Assert.validate_schema(res.json())


def test_single_user():
    res = api.single_user()
    res_body = res.json()
    assert res.status_code == HTTPStatus.OK
    # Assert.validate_schema(res.body)
    assert res_body["data"]["first_name"] == "Janet"
    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    assert example == res_body


def test_create():
    post = api.create("Margo", "waitress")
    # name = 'Margo'
    # job = 'waitress'
    # post_body = post.json()

    assert post.status_code == HTTPStatus.CREATED
    assert post.json()["name"] == "Margo"
    assert post.json()["job"] == "waitress"
    assert api.delete_user(post.json()['id']).status_code == HTTPStatus.NO_CONTENT




