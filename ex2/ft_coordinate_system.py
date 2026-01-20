#!/usr/bin/env python3

import sys  # Authorized (even if not used)
import math


def create_position(x: int, y: int, z: int) -> tuple:
    """Create an immutable 3D position (x, y, z)."""
    return (x, y, z)


def distance_3d(p1: tuple, p2: tuple) -> float:
    """Compute Euclidean distance between two 3D points."""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_str: str) -> tuple:
    """
    Parse a coordinate string like "3,4,0" into a tuple of ints (3, 4, 0).
    Raises ValueError if parsing fails.
    """
    parts = coord_str.split(",")
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)

    # 1) Create a position
    position = create_position(10, 20, 5)
    print(f"Position created: {position}")

    # 2) Distance between origin and created position (rounded like example: 22.91)
    d1 = distance_3d(origin, position)
    print(f"Distance between {origin} and {position}: {round(d1, 2)}")

    # 3) Parse valid coordinates
    valid_str = "3,4,0"
    print(f'Parsing coordinates: "{valid_str}"')
    parsed = parse_coordinates(valid_str)
    print(f"Parsed position: {parsed}")

    d2 = distance_3d(origin, parsed)
    print(f"Distance between {origin} and {parsed}: {round(d2, 2)}")

    # 4) Parse invalid coordinates gracefully
    invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')
    try:
        _ = parse_coordinates(invalid_str)
    except Exception as e:
        # Match the example style shown in the subject
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    # 5) Unpacking demonstration
    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
