#!/usr/bin/env python3

import sys
import math


def create_position(x: int, y: int, z: int) -> tuple:
    """
    Creates a 3D position represented as a tuple (x, y, z).
    """
    return (x, y, z)


def distance_3d(p1: tuple, p2: tuple) -> float:
    """
    Computes the Euclidean distance between two points in 3D space.
    """
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def fmt_dist(p1: tuple, p2: tuple) -> float:
    """
    Returns the distance between two 3D points rounded to two decimals.
    """
    return round(distance_3d(p1, p2), 2)


def parse_coordinates(coord_str: str) -> tuple:
    """
    Parses a string in the format 'x,y,z' and returns a 3D position tuple.

    Raises a ValueError if the format is invalid or values cannot be converted.
    """
    parts = coord_str.split(",")
    if len(parts) != 3:
        raise ValueError("Coordinates must be in the format x,y,z")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def main() -> None:
    """
    Demonstrates a simple 3D coordinate system.

    The program creates positions using tuples, computes the Euclidean
    distance between points, parses coordinates from strings, handles
    invalid input gracefully, and shows tuple unpacking in practice.
    """
    print("=== Game Coordinate System ===")
    print()

    origin = (0, 0, 0)

    position = create_position(10, 20, 5)
    print(f"Position created: {position}")
    print(f"Distance between {origin} and {position}: {fmt_dist(origin, position)}")
    print()

    valid_str = "3,4,0"
    print(f'Parsing coordinates: "{valid_str}"')
    parsed = parse_coordinates(valid_str)
    print(f"Parsed position: {parsed}")
    print(f"Distance between {origin} and {parsed}: {fmt_dist(origin, parsed)}")
    print()

    invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')
    try:
        parse_coordinates(invalid_str)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    print()

    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()


