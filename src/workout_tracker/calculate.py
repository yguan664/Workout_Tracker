def calculate_volume(record):
    """Calculate volume for one workout record."""
    return record["weight"] * record["reps"]


def summarize_by_exercise(records):
    """Summarize workout records by exercise."""
    summary = {}

    for record in records:
        exercise = record["exercise"]
        weight = record["weight"]
        reps = record["reps"]
        volume = calculate_volume(record)

        if exercise not in summary:
            summary[exercise] = {
                "max_weight": weight,
                "total_weight": weight,
                "count": 1,
                "total_reps": reps,
                "total_volume": volume,
            }
        else:
            if weight > summary[exercise]["max_weight"]:
                summary[exercise]["max_weight"] = weight

            summary[exercise]["total_weight"] += weight
            summary[exercise]["count"] += 1
            summary[exercise]["total_reps"] += reps
            summary[exercise]["total_volume"] += volume

    for exercise in summary:
        summary[exercise]["average_weight"] = (
            summary[exercise]["total_weight"] / summary[exercise]["count"]
        )
        del summary[exercise]["total_weight"]
        del summary[exercise]["count"]

    return summary


def calculate_total_volume(records):
    """Calculate total volume for all records."""
    total = 0

    for record in records:
        total += calculate_volume(record)

    return total


def filter_by_exercise(records, exercise_name):
    """Return records for one exercise."""
    filtered = []

    for record in records:
        if record["exercise"] == exercise_name:
            filtered.append(record)

    return filtered


def get_personal_records(records):
    """Get max weight for each exercise."""
    personal_records = {}

    for record in records:
        exercise = record["exercise"]
        weight = record["weight"]

        if exercise not in personal_records:
            personal_records[exercise] = weight
        elif weight > personal_records[exercise]:
            personal_records[exercise] = weight

    return personal_records