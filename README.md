Python Module 03 – Data Quest

This project is part of a structured Python learning curriculum.

The goal of this module is to consolidate Python fundamentals through
practical and progressive exercises, with a strong focus on
understanding, clarity, and the ability to explain technical decisions
during evaluation.

Each exercise is self-contained and designed to reinforce specific
concepts related to data processing, program flow, and error handling
in Python.

🎯 Objectives

Apply core Python concepts through small, focused exercises

Work with command-line input using sys.argv

Process and analyze data using appropriate data structures

Handle invalid input gracefully without crashing the program

Write clear, readable, and well-structured code

Develop the ability to explain design and implementation decisions

🧠 Topics covered

Command-line arguments (sys.argv)

Python collections:

lists for sequential data processing

tuples for structured and immutable data

Basic analytics (sum, average, min, max, range)

Error handling with try / except

Graceful program termination

Unpacking of tuples

Program execution flow and entry point

Code clarity and readability

🧪 Exercises overview
Exercise 0 – Command Quest

Concepts: sys.argv, program execution flow, loops

A command-line program that:

reads arguments passed from the terminal

distinguishes between the script name and user-provided arguments

handles the case where no arguments are given

displays structured output following the subject specifications

This exercise introduces how Python programs receive external input and
how to manage basic command-line interaction.

Exercise 1 – Score Analytics

Concepts: lists, basic statistics, try / except

A score analysis program that:

receives player scores from the command line

stores valid scores in a list

computes basic statistics (total, average, min, max, range)

handles invalid input gracefully without crashing

This exercise reinforces why lists are suitable for sequential data
processing and how to manage input errors in a controlled way.

Exercise 2 – Game Coordinate System

Concepts: tuples, unpacking, mathematical computation, error handling

A coordinate system program that:

represents 3D positions using tuples

calculates Euclidean distance between two points

parses coordinates from strings

handles invalid coordinate formats using exceptions

demonstrates tuple unpacking for clarity and readability

This exercise focuses on working with structured data and expressing
intent clearly when accessing coordinate components.

Exercise 3 – Achievement Tracker

Concepts: dictionaries, iteration, structured data

A program that tracks and processes player achievements using key-value
pairs, reinforcing the use of dictionaries for structured and labeled
data.

Exercise 4 – Inventory System

Concepts: data validation, collections, controlled updates

An inventory management program that demonstrates how to update and
validate stored data while maintaining program stability.

Exercise 5 – Data Stream

Concepts: iteration, data processing, robustness

A progressive data processing exercise focused on handling sequences of
input data in a safe and predictable way.

Exercise 6 – Analytics Dashboard

Concepts: aggregation, formatting, code organization

A final exercise that brings together multiple concepts from the module
to produce structured analytical output in a clear and readable format.

🗂️ Project structure
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

▶️ How to run

From the root of the project:

python3 ex01/ft_score_analytics.py 1500 2300 1800
python3 ex02/ft_coordinate_system.py

📌 Notes

All programs use only the Python standard library

The output format follows the subject requirements

No external dependencies are required




