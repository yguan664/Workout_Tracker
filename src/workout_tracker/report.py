def summarize_exercise(exercise_name, stats):
    """Format stats for one exercise."""
    lines = []
    lines.append(f"Exercise: {exercise_name}")
    lines.append(f"  Max Weight  : {stats['max_weight']}")
    lines.append(f"  Avg Weight  : {stats['average_weight']}")
    lines.append(f"  Total Reps  : {stats['total_reps']}")
    lines.append(f"  Total Volume: {stats['total_volume']}")
    return "\n".join(lines)


def summarize_all(all_stats):
    """Format stats for all exercises."""
    parts = []
    for exercise_name, stats in all_stats.items():
        parts.append(summarize_exercise(exercise_name, stats))
    return "\n\n".join(parts)


def summarize_total_volume(total_volume):
    """Format total volume."""
    return f"Total workout volume: {total_volume}"


def summarize_personal_records(personal_records):
    """Format personal records."""
    lines = ["Personal Records"]
    for exercise in personal_records:
        lines.append(f"{exercise}: {personal_records[exercise]}")
    return "\n".join(lines)