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