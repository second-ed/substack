import pytest

from substack.property_based_testing.change_of_state import Lock, State


def test_lock():
    lock = Lock()
    assert lock.state == State.OPEN
    lock.lock()
    assert lock.state == State.CLOSED


def test_unlock():
    lock = Lock()
    assert lock.state == State.OPEN
    lock.lock()
    assert lock.state == State.CLOSED
    lock.unlock()
    assert lock.state == State.OPEN


def test_multiple_locks():
    with pytest.raises(ValueError):
        Lock().lock().lock()


def test_unlock_already_open():
    with pytest.raises(ValueError):
        Lock().unlock()
