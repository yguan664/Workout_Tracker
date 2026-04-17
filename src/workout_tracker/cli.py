import sys

from workout_tracker.calculate import summarize_by_exercise
from workout_tracker.io import load_workouts
from workout_tracker.report import summarize_all


def main():
    """Run workouttracker command line interface."""
    if len(sys.argv) != 2:
        print("Usage: python -m workout_tracker.cli <csv_file>")
        return

    filepath = sys.argv[1]
    workouts = load_workouts(filepath)
    stats = summarize_by_exercise(workouts)
    report = summarize_all(stats)

    print(report)


if __name__ == "__main__":
    main()