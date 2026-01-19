#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Command Quest ===")

    args = sys.argv
    program_name = args[0]
    total_args = len(args)

    if total_args == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {total_args}")
        return

    print(f"Program name: {program_name}")
    print(f"Arguments received: {total_args - 1}")

    index = 1
    for arg in args[1:]:
        print(f"Argument {index}: {arg}")
        index += 1

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
