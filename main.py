# Abandon all hope, ye who enter here
import console
from typing import Callable


class MenuItem:
    def __init__(self, name: str, action: Callable):
        self.name = name
        self.action = action

    def __str__(self):
        return self.name


def show_menu(message: str, items: list[MenuItem]) -> None:
    if message:
        print(message)

    for i, item in enumerate(items):
        print(f"{i + 1} - {item}")

    choice = 0
    action: Callable
    while True:
        try:
            choice = int(input("Choice: ")) - 1
            action = items[choice].action
            break
        except (ValueError, IndexError):
            print("Invalid choice.")
    action()


def main() -> int:
    while True:
        console.clear()
        show_menu(
            "Main Menu",
            [
                MenuItem(
                    "Calculate AABB of a mesh", lambda: print("TODO: Implement.")
                ),  # TODO: Implement
                MenuItem("Exit", lambda: exit(0)),
            ],
        )


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt as e:
        print("User interrupted program.")
