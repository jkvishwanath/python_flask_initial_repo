# pylint: disable=redefined-outer-name
import pytest

from wholesale_store import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app_context = app.app_context()
    with app.test_client() as client:
        app_context.push()
        yield client
        app_context.pop()

