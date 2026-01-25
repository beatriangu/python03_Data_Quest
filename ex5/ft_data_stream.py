#!/usr/bin/env python3


def game_event_stream(total_events):
    """
    Generator that simulates a stream of game events.
    Each event is generated on demand using yield.
    """
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, total_events + 1):
        player = players[i % len(players)]
        level = (i * 3) % 15
        action = actions[i % len(actions)]
        yield i, player, level, action


def fibonacci():
    """
    Infinite Fibonacci generator.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_numbers():
    """
    Generator that yields prime numbers.
    """
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1


def main():
    print("=== Game Data Stream Processor ===\n")

    total_events = 1000
    print(f"Processing {total_events} game events...\n")

    high_level_players = 0
    treasure_events = 0
    level_up_events = 0
    processed_events = 0

    for event_id, player, level, action in game_event_stream(total_events):
        processed_events += 1

        if level >= 10:
            high_level_players += 1
        if action == "found treasure":
            treasure_events += 1
        if action == "leveled up":
            level_up_events += 1

        if event_id <= 3:
            print(
                f"Event {event_id}: Player {player} "
                f"(level {level}) {action}"
            )

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {processed_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}\n")

    print("Memory usage: Constant (streaming)")
    print("Processing time: Simulated\n")

    print("=== Generator Demonstration ===")

    fib = fibonacci()
    print("Fibonacci sequence (first 10):", end=" ")
    for _ in range(10):
        print(next(fib), end=", ")
    print()

    primes = prime_numbers()
    print("Prime numbers (first 5):", end=" ")
    for _ in range(5):
        print(next(primes), end=", ")
    print()


if __name__ == "__main__":
    main()
