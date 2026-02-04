from __future__ import annotations

from collections.abc import Hashable
from types import MappingProxyType

import attrs
import polars as pl
from attrs.validators import deep_mapping, instance_of, is_callable

from .io_funcs import READ_FUNCS, WRITE_FUNCS, Data, ReadFn, WriteFn


@attrs.define
class IoBase:
    read_fns: MappingProxyType[Hashable, ReadFn] = attrs.field(
        default=READ_FUNCS,
        validator=deep_mapping(
            key_validator=instance_of(Hashable),
            value_validator=is_callable(),
            mapping_validator=instance_of(MappingProxyType),
        ),
        converter=MappingProxyType,
    )
    write_fns: MappingProxyType[Hashable, WriteFn] = attrs.field(
        default=WRITE_FUNCS,
        validator=deep_mapping(
            key_validator=instance_of(Hashable),
            value_validator=is_callable(),
            mapping_validator=instance_of(MappingProxyType),
        ),
        converter=MappingProxyType,
    )

    def read(self, path: str, file_type: str) -> dict | pl.DataFrame:
        if file_type not in self.read_fns:
            raise NotImplementedError(f"{file_type = } not in {self.read_fns}")
        return self.read_fns[file_type](path)

    def write(self, data: dict | pl.DataFrame, path: str, file_type: str) -> None:
        if file_type not in self.read_fns:
            raise NotImplementedError(f"{file_type = } not in {self.write_fns}")
        return self.write_fns[file_type](data, path)


@attrs.define
class RealIoV2(IoBase):
    pass


@attrs.define
class FakeIoV2(IoBase):
    files: dict[str, Data] = attrs.field(factory=dict, validator=instance_of(dict))
    log: list[dict] = attrs.field(factory=list, validator=instance_of(list))

    def __attrs_post_init__(self) -> None:
        self.read_fns = MappingProxyType(dict.fromkeys(self.read_fns.keys(), self._read_fn))
        self.write_fns = MappingProxyType(dict.fromkeys(self.write_fns.keys(), self._write_fn))

    def _read_fn(self, path: str, file_type: str) -> dict | pl.DataFrame:
        self.log.append({"func": "read", "path": path, "file_type": file_type})
        return self.files[path]

    def _write_fn(self, data: dict | pl.DataFrame, path: str, file_type: str) -> None:
        self.log.append({"func": "write", "path": path, "file_type": file_type})
        self.files[path] = data
