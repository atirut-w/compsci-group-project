# Abandon all hope, ye who enter here
import console


def show_menu(message: str, items: list[str]) -> int:
    if message:
        print(message)

    for i, item in enumerate(items):
        print(f"{i + 1} - {item}")

    while True:
        try:
            choice = int(input("Choice: ")) - 1
            if choice in range(len(items)):
                return choice
            else:
                raise ValueError()
        except ValueError:
            print("Invalid choice.")


def main() -> int:
    while True:
        console.clear()

        match show_menu("Main Menu", ["Calculate AABB from OBJ mesh", "Exit"]):
            case 0:
                print("TODO: Implement")  # TODO: Implement
            case 1:
                return 0

    return 0


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt as e:
        print("User interrupted program.")
