# convert to dataclasses
from dataclasses import dataclass, field


@dataclass
class A:
    _length: int = field(init=False, default=0)
    # def __init__(self) -> None:
    #   self._length = 0


@dataclass
class B:
    x: int
    y: str = field(init=False, default="hello")
    l: list[int] = field(default_factory=list)
    # def __init__(self, x: int, y: str = "hello", l: list[int] | None = None) -> None:
    #   self.x = x
    #   self.y = y
    #   self.l = [] if not l else l


@dataclass
class C:
    a: int = 3
    b: int = field(init=False)
    # def __init__(self, a: int = 3) -> None:
    #     self.a = a
    #     self.b = a + 3
    def __post_init__(self) -> None:
        self.b = self.a + 3


a_inst = A()
print(a_inst)

b_inst = B(x=7)
print(b_inst)

c_inst = C(a=5)
print(c_inst)
