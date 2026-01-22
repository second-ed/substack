from substack.stateful_things.pt_1.adapters import FakeIo
from substack.stateful_things.pt_1.simple_usecase import some_usecase_fn


def test_some_usecase_fn() -> None:
    adapter = FakeIo(
        files={
            "path/to/read.json": {"a": 0, "b": 1, "c": [2, 3]},
        }
    )
    expected_result = {"a": 0, "b": 1, "c": [2, 3]}

    some_usecase_fn(
        config={
            "read_path": "path/to/read.json",
            "write_path": "path/to/write.json",
        },
        adapter=adapter,
    )
    assert adapter.files["path/to/write.json"] == expected_result
