def summarize_exercise(exercise_name, stats):
    lines = []
    lines.append(f"Exercise: {exercise_name}")
    lines.append(f"  Max Weight  : {stats['max_weight']}")
    lines.append(f"  Avg Weight  : {stats['average_weight']}")
    lines.append(f"  Total Reps  : {stats['total_reps']}")
    lines.append(f"  Total Volume: {stats['total_volume']}")
    return "\n".join(lines)


def summarize_all(all_stats):
    parts = []
    for exercise_name, stats in all_stats.items():
        parts.append(summarize_exercise(exercise_name, stats))
    return "\n\n".join(parts)