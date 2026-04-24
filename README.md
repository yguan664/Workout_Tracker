# 821_Final_Project
# Workout Tracker Library

This is a simple Python library for reading and analyzing workout records.

## Features

- Read workout data from a CSV file
- Validate input data (no negative weight, reps > 0, required columns)
- Compute workout volume (weight × reps)
- Summarize data by exercise (max, average, total reps, total volume)

### Additional Features

- Compute total workout volume across all records
- Filter records by exercise
- Get personal records (max weight per exercise)
- Generate a simple bar chart of total volume by exercise

- Print a report using a command line interface (CLI)

## Project Structure

src/workout_tracker/

- io.py (read CSV data)  
- calculate.py (compute statistics + helper functions)  
- report.py (format output)  
- plot.py (generate plots)  
- cli.py (command line interface)  

tests/

- test_io.py  
- test_calculate.py  
- test_report.py  
- test_plot.py  

data/

- sample_workouts.csv  

## How to Run Tests

Run this in the project root:

pytest

## How to Run the CLI

PYTHONPATH=src python -m workout_tracker.cli data/sample_workouts.csv

This will:

- Load workout data
- Print summary by exercise
- Print total workout volume
- Print personal records

## Example Output

Exercise: bench_press  
Max Weight : 190.0  
Avg Weight : 186.67  
Total Reps : 13  
Total Volume: 2420.0  

Exercise: squat  
Max Weight : 235.0  
Avg Weight : 230.0  
Total Reps : 8  
Total Volume: 1830.0  

Exercise: deadlift  
Max Weight : 275.0  
Avg Weight : 275.0  
Total Reps : 5  
Total Volume: 1375.0  

Overall Summary  
Total Workout Volume: 5625.0  

Personal Records:  
  bench_press: 190.0  
  squat: 235.0  
  deadlift: 275.0  

## How to Use Additional Functions

Example: filter records

from workout_tracker.io import load_workouts  
from workout_tracker.calculate import filter_by_exercise  

records = load_workouts("data/sample_workouts.csv")  
bench = filter_by_exercise(records, "bench_press")  

print(bench)  

## How to Generate Plot

from workout_tracker.io import load_workouts  
from workout_tracker.calculate import summarize_by_exercise  
from workout_tracker.plot import plot_total_volume  

records = load_workouts("data/sample_workouts.csv")  
stats = summarize_by_exercise(records)  

plot_total_volume(stats, "volume.png")  

This will create a bar chart image showing total volume for each exercise.

## Development Notes

- Code is written in a simple way (basic Python, no advanced libraries)
- We used csv, dict, and loops
- Plotting uses matplotlib
- Tests are written using pytest

## Generative AI Usage

See AI_USAGE.md for details.

## Group Members

- Weizhao Liu  
- Jack Guan