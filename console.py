import ansi


def clear() -> None:
    ansi.cup(1, 1)
    ansi.ed(2)
