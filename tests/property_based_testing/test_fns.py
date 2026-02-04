from pathlib import Path

import hypothesis.strategies as st
from hypothesis import given

from substack.property_based_testing.fns import lower_str


@given(inp_str=st.text())
def test_lower_str_idempotence(inp_str):
    assert lower_str(inp_str) == lower_str(lower_str(inp_str))


@given(inp_str=st.text())
def test_path_idempotence(inp_str):
    assert Path(inp_str) == Path(Path(inp_str))
