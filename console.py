from sys import stdout


def write_raw(data) -> None:
    stdout.buffer.write(data)
    stdout.flush()


def cup(n: int, m: int) -> None:
    write_raw(b"\x1b[%d;%dH" % (n, m))


def ed(n: int) -> None:
    write_raw(b"\x1b[%dJ" % n)


def clear() -> None:
    ed(2)
    cup(1,1)
