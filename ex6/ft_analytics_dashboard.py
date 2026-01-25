#!/usr/bin/env python3

def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    players = ["alice", "bob", "charlie", "diana"]
    scores = [2300, 1800, 2150, 2050]
    regions = ["north", "east", "north", "central"]

    active_players = ["alice", "bob", "charlie"]
    active_set = {p for p in active_players}

    achievements = [
        "first_kill",
        "level_10",
        "boss_slayer",
        "first_kill",
        "level_10",
    ]

    achievements_count = {
        "alice": 5,
        "bob": 3,
        "charlie": 7,
        "diana": 1,
    }

    # -----------------------------
    # List Comprehension Examples
    # -----------------------------
    print("=== List Comprehension Examples ===")

    high_scorers = [p for p, s in zip(players, scores) if s > 2000]
    scores_doubled = [s * 2 for s in scores]

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}\n")

    # -----------------------------
    # Dict Comprehension Examples
    # -----------------------------
    print("=== Dict Comprehension Examples ===")

    player_scores = {p: s for p, s in zip(players, scores)}

    score_categories = {
        "high": len([s for s in scores if s > 2000]),
        "medium": len([s for s in scores if 1500 <= s <= 2000]),
        "low": len([s for s in scores if s < 1500]),
    }

    achievement_counts = {
        player: achievements_count[player]
        for player in players
    }

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}\n")

    # -----------------------------
    # Set Comprehension Examples
    # -----------------------------
    print("=== Set Comprehension Examples ===")

    unique_players = {p for p in players}
    unique_achievements = {a for a in achievements}
    active_regions = {
        r for p, r in zip(players, regions)
        if p in active_set
    }

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}\n")

    # -----------------------------
    # Combined Analysis
    # -----------------------------
    print("=== Combined Analysis ===")

    total_players = len(players)
    average_score = sum(scores) / total_players
    top_score = max(scores)
    top_player = players[scores.index(top_score)]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {average_score:.1f}")
    print(
        f"Top performer: {top_player} "
        f"({top_score} points, {achievements_count[top_player]} achievements)"
    )


if __name__ == "__main__":
    main()
