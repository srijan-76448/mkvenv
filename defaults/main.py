import os

mainDir = os.path.abspath (os.path.dirname (__file__))

import setup
setup.main (mainDir)


def print_error (error: str):
    print (F"\033[1;31m[-] {error}\033[0m")


def print_success (succ: str):
    print (f"\033[1;32m[+] {succ}\033[0m")


def main ():
    # write your code
    pass


if __name__ == "__main__":
    main ()
