import os, setup

mainDir = os.path.abspath(os.path.dirname(__file__))
setup.main(mainDir)


def print_error(error: str):
    print(f"\033[38;2;255;0;0;1m[-] {error}\033[0m")


def print_success(succ: str):
    print(f"\033[38;2;0;255;0;1m[-] {succ}\033[0m")


def main():
    # write your code
    pass


if __name__ == "__main__":
    main()
