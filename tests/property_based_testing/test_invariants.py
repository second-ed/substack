import hypothesis.strategies as st
from hypothesis import given


@given(st.lists(st.integers()))
def test_sort_preserves_length(xs):
    assert len(sorted(xs)) == len(xs)
