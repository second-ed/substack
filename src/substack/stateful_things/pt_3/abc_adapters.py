from __future__ import annotations

import json
from pathlib import Path
from typing import Protocol, runtime_checkable

import polars as pl


@runtime_checkable
class IoProtocol(Protocol):
    def read_json(self, path: str) -> dict: ...
    def write_json(self, data: dict, path: str) -> None: ...
    def read_parquet(self, path: str) -> pl.DataFrame: ...
    def write_parquet(self, data: pl.DataFrame, path: str) -> None: ...


class RealIo:
    def read_json(self, path: str) -> dict:
        return json.loads(Path(path).read_text())

    def write_json(self, data: dict, path: str) -> None:
        Path(path).write_text(json.dumps(data))

    def read_parquet(self, path: str) -> pl.DataFrame:
        return pl.read_parquet(path)

    def write_parquet(self, data: pl.DataFrame, path: str) -> None:
        data.to_parquet(path)


class FakeIo:
    def __init__(self, files: dict | None = None) -> None:
        self.files = files or {}

    def read_json(self, path: str) -> dict:
        return self.files[path]

    def write_json(self, data: dict, path: str) -> None:
        self.files[path] = data

    def read_parquet(self, path: str) -> pl.DataFrame:
        return self.files[path]

    def write_parquet(self, data: pl.DataFrame, path: str) -> None:
        self.files[path] = data
