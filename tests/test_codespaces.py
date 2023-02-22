from datasette.app import Datasette
import pytest
from unittest import mock
import os


@pytest.mark.asyncio
async def test_no_env_variable():
    datasette = Datasette(memory=True)
    response = await datasette.client.get("/-/actor.json")
    assert response.status_code == 200
    assert response.json() == {"actor": None}


@pytest.mark.asyncio
async def test_codespace_name():
    with mock.patch.dict(os.environ, {"CODESPACE_NAME": "test-codespace"}):
        datasette = Datasette(memory=True)
        response = await datasette.client.get("/-/actor.json")
        assert response.status_code == 200
        assert response.json() == {"actor": {"id": "root"}}
