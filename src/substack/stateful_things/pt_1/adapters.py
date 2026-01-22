from __future__ import annotations

import json
from pathlib import Path
from typing import Protocol, runtime_checkable


@runtime_checkable
class IoProtocol(Protocol):
    def read_json(self, path: str) -> dict: ...
    def write_json(self, data: dict, path: str) -> None: ...


class RealIo:
    def read_json(self, path: str) -> dict:
        return json.loads(Path(path).read_text())

    def write_json(self, data: dict, path: str) -> None:
        Path(path).write_text(json.dumps(data))


class FakeIo:
    def __init__(self, files: dict | None = None) -> None:
        self.files = files or {}

    def read_json(self, path: str) -> dict:
        return self.files[path]

    def write_json(self, data: dict, path: str) -> None:
        self.files[path] = data
