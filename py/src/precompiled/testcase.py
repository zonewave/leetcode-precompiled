from typing import Generic, TypeVar, Tuple, Any


R = TypeVar('R')
ArgsType = TypeVar('ArgsType')


class ArgsHolder(Generic[ArgsType]):
    def __init__(self, *args: ArgsType):
        self.args: Tuple[ArgsType, ...] = args

    def get(self, index: int) -> Any:
        return self.args[index]


class LTestCase(Generic[R, ArgsType]):
    name: str
    args: ArgsHolder[ArgsType]
    want: R

    def __init__(self, name: str, want: R, *args: ArgsType):
        self.name = name
        self.want = want
        self.args = ArgsHolder(*args)
