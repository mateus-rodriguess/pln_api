import pytest

@pytest.fixture(scope="module")
def test_create_user(test_client_app, data_user):
    response = test_client_app.post("/auth/sign-up", json=data_user)
    yield response


def test_user_list(test_client_app, test_create_user):
    response = test_client_app.get("users")
    assert response.status_code == 200