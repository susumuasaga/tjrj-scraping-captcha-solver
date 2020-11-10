import pytest
from snapshottest.module import SnapshotTest

import captcha_distortion
import noise_filter
import ocr
import consulta_processo
from FakeSession import FakeSession
from mixed_decoder import mixed_decoder
import codecs

pytestmark = pytest.mark.asyncio
codecs.register_error("mixed", mixed_decoder)
session = FakeSession()


@pytest.fixture()
def mock_ocr(monkeypatch):
    monkeypatch.setattr(captcha_distortion, "undistort", lambda image: image)
    monkeypatch.setattr(noise_filter, "clean", lambda image: image)
    monkeypatch.setattr(ocr, "read", lambda image: ("327gv25", 50))


async def test_parse_process_page1(snapshot: SnapshotTest, mock_ocr):
    snapshot.assert_match(
        (await consulta_processo.parse("2014.038.068873-6", session)).dict()
    )


async def test_parse_process_page2(snapshot: SnapshotTest, mock_ocr):
    snapshot.assert_match(
        (await consulta_processo.parse("2015.001.008715-3", session)).dict()
    )


async def test_parse_process_page3(snapshot: SnapshotTest, mock_ocr):
    snapshot.assert_match(
        (await consulta_processo.parse("2015.001.002715-6", session)).dict()
    )


async def test_parse_process_page4(snapshot: SnapshotTest, mock_ocr):
    snapshot.assert_match(
        (await consulta_processo.parse("2018.001.005599-7", session)).dict()
    )


async def test_parse_process_page5(snapshot: SnapshotTest, mock_ocr):
    assert await consulta_processo.parse("2008.900.001265-4", session) is None


async def test_parse_process_page6(snapshot: SnapshotTest, mock_ocr):
    snapshot.assert_match(
        (await consulta_processo.parse("2002.204.002450-8", session)).dict()
    )


async def test_parse_process_page7(snapshot: SnapshotTest, mock_ocr):
    assert await consulta_processo.parse("2000.202.007802-7", session) is None


async def test_parse_process_page8(snapshot: SnapshotTest, mock_ocr):
    assert await consulta_processo.parse("2010.067.002663-6", session) is None
