from __future__ import annotations

import json
from collections.abc import Callable
from enum import Enum, unique
from pathlib import Path

import polars as pl

from .registries import register_read_fn, register_write_fn

type Data = dict | pl.DataFrame
type ReadFn = Callable[[str], Data]
type WriteFn = Callable[[Data, str], None]


@unique
class FileType(Enum):
    JSON = "json"
    PARQUET = "parquet"


@register_read_fn(FileType.JSON)
def read_json(path: str) -> dict:
    return json.loads(Path(path).read_text())


@register_write_fn(FileType.JSON)
def write_json(data: dict, path: str) -> None:
    Path(path).write_text(json.dumps(data))


@register_read_fn(FileType.PARQUET)
def read_parquet(path: str) -> pl.DataFrame:
    return pl.read_parquet(path)


@register_write_fn(FileType.PARQUET)
def write_parquet(data: pl.DataFrame, path: str) -> None:
    data.to_parquet(path)
