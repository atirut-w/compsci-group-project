# Abandon all hope, ye who enter here
def main() -> int:
    return 0


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt as e:
        print("User interrupted program.")
