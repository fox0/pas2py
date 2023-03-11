import pytest

from main import main


def _compare(filename: str):
    with open(f'tests/{filename}.pas') as f, open(f'tests/{filename}.py') as fpy:
        text = f.read()
        expected = fpy.read()
    assert main(text) == expected


def test001():
    _compare('001')


def test002():
    _compare('002')


@pytest.mark.skip(reason="bug =")
def test003():
    _compare('003')


def test004():
    _compare('004')


def test005_real():
    _compare('005_real')


@pytest.mark.skip(reason="bug =")
def test006_for():
    _compare('006_for')
