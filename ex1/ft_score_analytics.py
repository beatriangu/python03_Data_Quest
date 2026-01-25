#!/usr/bin/env python3

import sys


def main() -> None:
    """
    Reads player scores from the command line and displays basic statistics.

    The program first checks whether any arguments are provided.
    Each argument is then converted to an integer while handling
    possible conversion errors using try/except.

    Once the input data is validated, all calculations are performed
    using the processed values instead of accessing sys.argv directly.
    """

    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid score: '{arg}' is not an integer")
            return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    high_score = max(scores)
    low_score = min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}")


if __name__ == "__main__":
    main()
