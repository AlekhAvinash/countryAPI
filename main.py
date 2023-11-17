#!/usr/bin/python3

from random import choice
from quests import QTS


def getinp():
    n = 5
    while n:
        try:
            out = int(input("Enter a number between [1-4]: "))
            if out not in range(1, 5):
                raise ValueError
            return out
        except ValueError:
            print(f"Invalid Input!! {n} tries left.")
        n -= 1
    return 0


def main(ctr):
    pts = 0
    for i in range(ctr):
        print("---" * 10)
        print(f"[i] Question {i+1}/{ctr}!!")
        print("---" * 10)
        qt = choice(QTS)()
        print(qt)
        out = getinp()
        if out and qt.check(out - 1):
            print("[+] Correct!!")
            pts += 1
        elif out and not qt.check(out - 1):
            print("[+] False.")
        else:
            print("[-] Input Error. Exiting.")
            return 0
    return pts


if __name__ == "__main__":
    ret = main(20)
    print(f"[i] Your score is: {ret}")
