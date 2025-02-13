__all__ = ["Ok", "Fail"]

from typing import Any, Generic, TypeVar

T = TypeVar("T")
F = TypeVar("F")


class Ok(Generic[T]):
    __data: T

    def __init__(self, data: T, /) -> None:
        self.__data = data

    def is_ok(self) -> bool:
        return True

    def unwrap(self) -> T:
        return self.__data

    def unwrap_fail(self) -> Any:
        raise Exception("Unwrapping Ok Result")

    def unwrap_or(self, default: T) -> T:
        return self.__data


class Fail(Generic[F]):
    __fail: F

    def __init__(self, fail: F, /) -> None:
        self.__fail = fail

    def is_ok(self) -> bool:
        return False

    def unwrap(self) -> Any:
        raise Exception("Unwrapping Fail result")

    def unwrap_fail(self) -> F:
        return self.__fail

    def unwrap_or(self, default: T) -> T:
        return default
