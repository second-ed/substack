from __future__ import annotations

import polars as pl

from .io_funcs import READ_FUNCS, WRITE_FUNCS, ReadFn, WriteFn


class IoBase:
    def __init__(
        self,
        read_fns: dict[str, ReadFn] = READ_FUNCS,
        write_fns: dict[str, WriteFn] = WRITE_FUNCS,
    ) -> None:
        self.read_fns = read_fns
        self.write_fns = write_fns

    def read(self, path: str, file_type: str) -> dict | pl.DataFrame:
        if file_type not in self.read_fns:
            raise NotImplementedError(f"{file_type = } not in {self.read_fns}")
        return self.read_fns[file_type](path)

    def write(self, data: dict | pl.DataFrame, path: str, file_type: str) -> None:
        if file_type not in self.read_fns:
            raise NotImplementedError(f"{file_type = } not in {self.write_fns}")
        return self.write_fns[file_type](data, path)


class RealIoV2(IoBase):
    pass


class FakeIoV2(IoBase):
    def __init__(
        self,
        read_fns: dict[str, ReadFn] = READ_FUNCS,
        write_fns: dict[str, WriteFn] = WRITE_FUNCS,
    ) -> None:
        self.read_fns = dict.fromkeys(read_fns, self._read_fn)
        self.write_fns = dict.fromkeys(write_fns, self._write_fn)

    def _read_fn(self, path: str, file_type: str) -> dict | pl.DataFrame:
        self.log.append({"func": "read", "path": path, "file_type": file_type})
        return self.files[path]

    def _write_fn(self, data: dict | pl.DataFrame, path: str, file_type: str) -> None:
        self.log.append({"func": "write", "path": path, "file_type": file_type})
        self.files[path] = data
