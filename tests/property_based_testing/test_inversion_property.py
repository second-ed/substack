import hypothesis.strategies as st
from hypothesis import given


@given(st.text())
def test_encode_decode_roundtrip(s):
    assert s.encode("utf-8").decode("utf-8") == s
