# 821_Final_Project
# Workout Tracker Library

This is a simple Python library for reading and analyzing workout records.

## Features

- Read workout data from a CSV file
- Validate input data (no negative weight, reps > 0, required columns)
- Compute workout volume (weight × reps)
- Summarize data by exercise (max, average, total reps, total volume)
- Print a simple report from the command line

## Project Structure
src/workout_tracker/
io.py # read CSV data
calculate.py # compute statistics
report.py # format output
cli.py # command line interface

tests/
test_io.py
test_calculate.py
test_report.py

data/
sample_workouts.csv

## How to Run Tests

Run this in the project root:
pytest


## How to Run the CLI

Example:


PYTHONPATH=src python -m workout_tracker.cli data/sample_workouts.csv


This will load the data and print summary for each exercise.

## Example Output


Exercise: bench_press
Max Weight : 190.0
Avg Weight : 186.67
Total Reps : 13
Total Volume: 2420.0


## Development Notes

- Code is written in a simple way (basic Python, no advanced libraries)
- We used `csv`, `dict`, and loops for implementation
- Tests are written using `pytest`

## Generative AI Usage

We used ChatGPT to:

- help design the project structure
- suggest function implementations
- debug errors (imports, pytest issues)
- improve README and workflow

All code was reviewed and tested by us before committing.

## Group Members

- Weizhao Liu
- Jack Guan
