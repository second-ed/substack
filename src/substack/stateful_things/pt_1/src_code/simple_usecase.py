from src_code.adapters import IoProtocol, RealIo


def some_usecase_fn(
    config: dict[str, str],
    adapter: IoProtocol,
) -> None:
    data = adapter.read_json(config["read_path"])

    # some business logic

    return adapter.write_json(data, config["write_path"])


if __name__ == "__main__":
    some_usecase_fn(
        config={
            "read_path": "path/to/read.json",
            "write_path": "path/to/write.json",
        },
        adapter=RealIo(),
    )
