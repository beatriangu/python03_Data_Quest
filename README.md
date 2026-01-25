🐍 Python Module 03 – Data Quest

This project is part of a structured Python learning curriculum.

The goal of Python Module 03 – Data Quest is to consolidate Python fundamentals through practical and progressive exercises, with a strong focus on:

understanding core concepts

writing clear, readable code

making conscious design decisions

being able to explain those decisions clearly during evaluation

Each exercise is self-contained and designed to reinforce specific concepts related to data processing, collections, program flow, and robust error handling in Python.

The module prioritizes clarity, correctness, and explainability over complex or overengineered solutions.

🎯 Objectives

Apply core Python concepts through small, focused exercises

Work with command-line input using sys.argv

Process and analyze data using appropriate data structures

Handle invalid input gracefully without crashing the program

Write clear, readable, and well-structured code

Develop the ability to justify design and implementation decisions

🧠 Topics Covered

Command-line arguments (sys.argv)

Python collections:

lists for sequential data processing

tuples for structured and immutable data

sets for uniqueness and analytics

dictionaries for structured and labeled data

Basic analytics (sum, average, min, max, range)

Error handling with try / except

Graceful program termination

Tuple unpacking for clarity and expressiveness

Program execution flow and entry point

Code clarity, readability, and explainability

🧪 Exercises Overview
🧭 Exercise 0 – Command Quest

Concepts: sys.argv, program execution flow, loops

A command-line program that:

reads arguments passed from the terminal

distinguishes between the script name and user-provided arguments

handles the case where no arguments are given

displays structured output following the subject specifications

This exercise introduces how Python programs receive external input and how to manage basic command-line interaction.

📊 Exercise 1 – Score Analytics

Concepts: lists, basic statistics, try / except

A score analysis program that:

receives player scores from the command line

stores valid scores in a list

computes basic statistics (total, average, min, max, range)

handles invalid input gracefully without crashing

This exercise reinforces why lists are suitable for sequential data processing and how to manage input errors in a controlled and predictable way.

📐 Exercise 2 – Game Coordinate System

Concepts: tuples, unpacking, mathematical computation, error handling

A coordinate system program that:

represents 3D positions using tuples

calculates Euclidean distance between two points

parses coordinates from strings

handles invalid coordinate formats using exceptions

demonstrates tuple unpacking for clarity and readability

This exercise focuses on working with structured data and expressing intent clearly when accessing coordinate components.

🏆 Exercise 3 – Achievement Tracker

Concepts: sets, set operations, analytics

A program that tracks and analyzes player achievements using sets to:

automatically remove duplicates

compute all unique achievements

find achievements common to multiple players

identify rare achievements

This exercise highlights how union, intersection, and difference can be used to perform analytics without complex loops.

🎒 Exercise 4 – Inventory Master

Concepts: dictionaries, nested data structures, controlled updates

An inventory management program that:

models player inventories using nested dictionaries

tracks item quantities, categories, rarity, and values

calculates total inventory value and item count

organizes items by category

performs a controlled transaction between players

produces a final analytics summary (most valuable player, most items, rarest items)

This exercise demonstrates how dictionaries can model complex relationships while keeping the code readable and aligned with the subject.

🌊 Exercise 5 – Data Stream

Concepts: iteration, data processing, robustness

A progressive data processing exercise focused on:

iterating over sequences of input data

processing data incrementally

handling edge cases safely

ensuring predictable and stable program behavior

This exercise introduces a streaming-oriented way of thinking about data processing.

📈 Exercise 6 – Analytics Dashboard

Concepts: comprehensions, aggregation, formatting, code organization

A final exercise that brings together multiple concepts from the module to:

demonstrate list, dict, and set comprehensions

aggregate and analyze data

present structured analytical output

reinforce clean organization and readability

This exercise emphasizes clarity of intent and mastery of Python comprehensions.

🗂️ Project Structure
.
├── ex00/
│   └── ft_command_quest.py
├── ex01/
│   └── ft_score_analytics.py
├── ex02/
│   └── ft_coordinate_system.py
├── ex03/
│   └── ft_achievement_tracker.py
├── ex04/
│   └── ft_inventory_system.py
├── ex05/
│   └── ft_data_stream.py
├── ex06/
│   └── ft_analytics_dashboard.py
├── README.md
├── FAQ.txt
└── FLO.txt


Each exercise can be executed independently from the project root.

▶️ How to Run

From the root of the project:

python3 ex01/ft_score_analytics.py 1500 2300 1800
python3 ex02/ft_coordinate_system.py

📌 Notes

All programs use only the Python standard library

The output format strictly follows the subject requirements

No external dependencies are required

The project prioritizes clarity, correctness, and explainability over overengineering





