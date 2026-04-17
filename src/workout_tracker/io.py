import csv


def load_workouts(filepath):
    workouts = []
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if "date" not in row or "exercise" not in row or "weight" not in row or "reps" not in row:
                raise ValueError("missing column in row")
            if float(row["weight"]) < 0:
                raise ValueError("weight cannot be negative")
            if int(row["reps"]) <= 0:
                raise ValueError("reps must be greater than 0")
            workouts.append({
                "date": row["date"],
                "exercise": row["exercise"],
                "weight": float(row["weight"]),
                "reps": int(row["reps"]),
            })
    return workouts