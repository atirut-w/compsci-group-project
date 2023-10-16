# Abandon all hope, ye who enter here
import console
from typing import Callable
from obj import Obj, Vector3


class MenuItem:
    def __init__(self, name: str, action: Callable[[], None]):
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


def do_aabb() -> None:
    path = input("Enter OBJ file path: ")

    try:
        obj = Obj.from_file(path)

        min_vert = Vector3(float("inf"), float("inf"), float("inf"))
        max_vert = Vector3(float("-inf"), float("-inf"), float("-inf"))

        for vert in obj.vertices:
            min_vert.x = min(min_vert.x, vert.x)
            min_vert.y = min(min_vert.y, vert.y)
            min_vert.z = min(min_vert.z, vert.z)

            max_vert.x = max(max_vert.x, vert.x)
            max_vert.y = max(max_vert.y, vert.y)
            max_vert.z = max(max_vert.z, vert.z)

        print(f"Calculated AABB for {len(obj.vertices)} vertices:")
        print(f"\tBounds: {min_vert} - {max_vert}")
        print(f"\tCenter: {(min_vert + max_vert) / 2}")
        print(f"\tSize: {max_vert - min_vert}")
    except FileNotFoundError:
        print("File not found.")

    input("Press enter to continue...")


def do_number_guess() -> None:
    from random import randint

    print("Guess a number between 1 and 10.")
    number = randint(1, 10)
    attempts = 0
    max_attempts: int
    if randint(0, 4) == 0:
        print("HARD MODE UNLOCKED")
        max_attempts = 3
    else:
        max_attempts = 5

    while attempts < max_attempts:
        while True:
            try:
                print(f"Attempts left: {max_attempts - attempts}")
                guess = int(input("Guess: "))
                if not guess in range(1, 21):
                    raise ValueError
                break
            except ValueError:
                print("Invalid guess.")

        if guess == number:
            print(f"You win! Took you {attempts + 1} attempts.")
            break
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")
        attempts += 1

    if attempts == max_attempts:
        print(f"You lose. The number was {number}.")
    input("Press enter to continue...")


def main() -> int:
    while True:
        console.clear()
        show_menu(
            "Main Menu",
            [
                MenuItem("Calculate AABB of a mesh", do_aabb),
                MenuItem("Number guessing game", do_number_guess),
                MenuItem("Exit", lambda: exit(0)),
            ],
        )


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt as e:
        print("User interrupted program.")
