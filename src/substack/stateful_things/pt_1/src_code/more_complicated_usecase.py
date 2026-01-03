from src_code.adapters import IoProtocol, RealIo


def some_other_usecase_fn(
    config: dict[str, str],
    adapter: IoProtocol,
) -> None:
    data = adapter.read_json(config["read_path"])
    other_data = adapter.read_json(config["other_read_path"])

    # some business logic
    updated_data = {**data, **other_data}

    adapter.write_json(updated_data, config["write_path"])


if __name__ == "__main__":
    some_other_usecase_fn(
        config={
            "read_path": "path/to/read.json",
            "other_read_path": "path/to/read_second.json",
            "write_path": "path/to/write.json",
        },
        adapter=RealIo(),
    )
