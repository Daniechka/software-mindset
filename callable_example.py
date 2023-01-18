from typing import Callable, Iterable


def f1(a: int):
    print("Call f1, got", a)


def f2(a: int):
    print("Call f2, got", a)


def f3(a: int):
    print("Call f3, got", a)


PostProcFunc = Callable[[int], None]
POST_PROCS = [f1, f2, f3]


def do_funcs(a: int, post_procs: Iterable[PostProcFunc]):
    for post_proc in post_procs:
        post_proc(a)


def main():
    myvar = 10
    do_funcs(myvar, POST_PROCS)


if __name__ == "__main__":
    main()
