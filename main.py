# Abandon all hope, ye who enter here
import console
from typing import Callable, Any
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


def do_knockoff_forth() -> None:
    stack: list[str] = []
    words: dict[str, list[str]] = {}

    def pop_operands() -> tuple[str, str]:
        try:
            rhs = stack.pop()
            return stack.pop(), rhs
        except IndexError:
            raise ValueError("Stack underflow.")

    def eval_word(word: str) -> None:
        match word:
            case "duck": # Super secret word. Prints the meowing duck.
                print("    _")
                print(".__(.)< (MEOW)")
                print(" \\___)")
            case "stack":
                padding = len(str(len(stack)))

                print("---- TOP OF STACK ----")
                for i, item in enumerate(stack):
                    print(f"{i:0{padding}}: {item}")
                print("---- BOTTOM OF STACK ----")
            case "pop":
                try:
                    print(stack.pop())
                except IndexError:
                    print("Stack underflow.")
            case "clear":
                stack.clear()
            case "+":
                lhs, rhs = pop_operands()
                result = int(lhs) + int(rhs)
                stack.append(str(result))
            case "-":
                lhs, rhs = pop_operands()
                result = int(lhs) - int(rhs)
                stack.append(str(result))
            case "*":
                lhs, rhs = pop_operands()
                result = int(lhs) * int(rhs)
                stack.append(str(result))
            case "/":
                lhs, rhs = pop_operands()
                result = int(lhs) / int(rhs)
                stack.append(str(result))
            case _:  # Not a built-in word
                if word in words:
                    for subword in words[word]:
                        eval_word(subword)
                else:
                    stack.append(word)

    print("[ Knockoff Forth ]")
    print("Enter words to evaluate them. Enter `exit` to stop.")
    print("Enter `stack` to print the stack, `pop` to discard the bottom item, and `clear` to clear the stack.")
    print("Dev notes: only math operations are supported. No macros, variables, etc. at this time.")
    print("When doing math ops, the bottom of the stack is popped first as the right-hand side, then the left-hand side is popped next.")
    while True:
        line = input("> ")
        
        for word in line.split():
            if word == "exit":
                return

            try:
                eval_word(word)
            except Exception as e:
                print(f"Eval error: {e}")


def do_avg() -> None:
    print("Enter numbers to calculate their average. Enter `q` to stop.")
    numbers: list[int] = []

    while True:
        try:
            number = input("Number: ")
            if number == "q":
                break
            numbers.append(int(number))
        except ValueError:
            print("Invalid number.")

    print(f"Average: {sum(numbers) / len(numbers)}")
    input("Press enter to continue...")


def main() -> int:
    while True:
        console.clear()
        show_menu(
            "Main Menu",
            [
                MenuItem("Calculate AABB of a mesh", do_aabb),
                MenuItem("Knockoff Forth", do_knockoff_forth),
                MenuItem("Calculate average of numbers", do_avg),
                MenuItem("Exit", lambda: exit(0)),
            ],
        )


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt as e:
        print("User interrupted program.")
