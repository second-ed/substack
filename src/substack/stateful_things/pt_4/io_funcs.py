from __future__ import annotations

import json
from collections.abc import Callable
from enum import Enum, unique
from pathlib import Path

import polars as pl

type Data = dict | pl.DataFrame
type ReadFn = Callable[[str], Data]
type WriteFn = Callable[[Data, str], None]


@unique
class FileType(Enum):
    JSON = "json"
    PARQUET = "parquet"


def read_json(path: str) -> dict:
    return json.loads(Path(path).read_text())


def write_json(data: dict, path: str) -> None:
    Path(path).write_text(json.dumps(data))


def read_parquet(path: str) -> pl.DataFrame:
    return pl.read_parquet(path)


def write_parquet(data: pl.DataFrame, path: str) -> None:
    data.to_parquet(path)


READ_FUNCS: dict[str, ReadFn] = {
    FileType.JSON: read_json,
    FileType.PARQUET: read_parquet,
}

WRITE_FUNCS: dict[str, WriteFn] = {
    FileType.JSON: write_json,
    FileType.PARQUET: write_parquet,
}
