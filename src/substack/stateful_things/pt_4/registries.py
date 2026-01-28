from __future__ import annotations

from collections.abc import Callable, Hashable

from .io_funcs import ReadFn, WriteFn

READ_FUNCS: dict[Hashable, ReadFn] = {}
WRITE_FUNCS: dict[Hashable, WriteFn] = {}


def register_read_fn(key: Hashable) -> Callable:
    key = standardise_key(key)

    def wrapper(func: Callable) -> Callable:
        READ_FUNCS[key] = func
        return func

    return wrapper


def register_write_fn(key: Hashable) -> Callable:
    key = standardise_key(key)

    def wrapper(func: Callable) -> Callable:
        WRITE_FUNCS[key] = func
        return func

    return wrapper


def standardise_key(key: Hashable) -> Hashable:
    return key.strip().lower() if isinstance(key, str) else key
