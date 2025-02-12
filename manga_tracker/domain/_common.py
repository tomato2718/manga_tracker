__all__ = ["Result"]

from typing import Generic, Protocol, TypeVar

DataType = TypeVar("DataType")
FailType = TypeVar("FailType", covariant=True)


class Result(Protocol, Generic[DataType, FailType]):
    def is_ok(self) -> bool: ...

    def unwrap(self) -> DataType: ...

    def unwrap_fail(self) -> FailType: ...

    def unwrap_or(self, default: DataType) -> DataType: ...
