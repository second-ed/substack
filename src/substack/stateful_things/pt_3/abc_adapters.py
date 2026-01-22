from __future__ import annotations

import json
from abc import ABC, abstractmethod
from pathlib import Path

import polars as pl


class IoBase(ABC):
    @abstractmethod
    def read(self, path: str, file_type: str) -> dict | pl.DataFrame: ...
    @abstractmethod
    def write(self, data: dict | pl.DataFrame, path: str, file_type: str) -> None: ...


class RealIoV2(IoBase):
    def read(self, path: str, file_type: str) -> dict | pl.DataFrame:
        if file_type == "json":
            return json.loads(Path(path).read_text())
        if file_type == "parquet":
            return pl.read_parquet(path)
        raise ValueError(f"given invalid {file_type = }")

    def write(self, data: dict | pl.DataFrame, path: str, file_type: str) -> None:
        if file_type == "json":
            Path(path).write_text(json.dumps(data))
        elif file_type == "parquet":
            data.to_parquet(path)
        raise ValueError(f"given invalid {file_type = }")


class FakeIoV2(IoBase):
    def __init__(self, files: dict | None = None) -> None:
        self.files = files or {}
        self.log = []

    def read(self, path: str, file_type: str) -> dict | pl.DataFrame:
        self.log.append({"func": "read", "path": path, "file_type": file_type})
        return self.files[path]

    def write(self, data: dict | pl.DataFrame, path: str, file_type: str) -> None:
        self.log.append({"func": "write", "path": path, "file_type": file_type})
        self.files[path] = data
