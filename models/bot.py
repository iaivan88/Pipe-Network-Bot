from typing import Literal, TypedDict


ModuleType = Literal["register", "tasks", "stats", "accounts"]


class OperationResult(TypedDict):
    identifier: str
    data: str
    status: bool

