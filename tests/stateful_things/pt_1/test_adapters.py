import pytest

from substack.stateful_things.pt_1.adapters import FakeIo, IoProtocol, RealIo


@pytest.mark.parametrize(
    ("impl", "protocol"),
    [
        pytest.param(
            RealIo,
            IoProtocol,
            id="ensure `RealIo` matches `IoProtocol`",
        ),
        pytest.param(
            FakeIo,
            IoProtocol,
            id="ensure `FakeIo` matches `IoProtocol`",
        ),
    ],
)
def test_adapter_protocols(impl, protocol):
    assert isinstance(impl, protocol)
