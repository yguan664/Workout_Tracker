import sys

from workout_tracker.calculate import (
    calculate_total_volume,
    get_personal_records,
    summarize_by_exercise,
)
from workout_tracker.io import load_workouts
from workout_tracker.report import summarize_all


def main():
    """Run the workout tracker command line interface."""
    if len(sys.argv) != 2:
        print("Usage: python -m workout_tracker.cli <csv_file>")
        return

    filepath = sys.argv[1]
    workouts = load_workouts(filepath)

    stats = summarize_by_exercise(workouts)
    report = summarize_all(stats)

    total_volume = calculate_total_volume(workouts)
    personal_records = get_personal_records(workouts)

    print(report)

    print("Overall Summary")
    print(f"Total Workout Volume: {total_volume}")
    print("Personal Records:")

    for exercise in personal_records:
        print(f"  {exercise}: {personal_records[exercise]}")


if __name__ == "__main__":
    main()