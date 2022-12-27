from __future__ import annotations

from app import index


def test_index():
    assert index() == 'Hello world'
