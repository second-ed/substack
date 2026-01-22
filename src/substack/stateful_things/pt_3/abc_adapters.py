from __future__ import annotations

import json
from abc import ABC, abstractmethod
from pathlib import Path

import polars as pl


class IoBase(ABC):
    @abstractmethod
    def read_json(self, path: str) -> dict: ...
    @abstractmethod
    def write_json(self, data: dict, path: str) -> None: ...
    @abstractmethod
    def read_parquet(self, path: str) -> pl.DataFrame: ...
    @abstractmethod
    def write_parquet(self, data: pl.DataFrame, path: str) -> None: ...


class RealIo(IoBase):
    def read_json(self, path: str) -> dict:
        return json.loads(Path(path).read_text())

    def write_json(self, data: dict, path: str) -> None:
        Path(path).write_text(json.dumps(data))

    def read_parquet(self, path: str) -> pl.DataFrame:
        return pl.read_parquet(path)

    def write_parquet(self, data: pl.DataFrame, path: str) -> None:
        data.to_parquet(path)


class FakeIo(IoBase):
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
