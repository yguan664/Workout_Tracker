from workout_tracker.calculate import calculate_volume, summarize_by_exercise


def test_calculate_volume():
    record = {
        "date": "2026-04-01",
        "exercise": "bench_press",
        "weight": 185.0,
        "reps": 5,
    }

    assert calculate_volume(record) == 925.0


def test_summarize_by_exercise_one_exercise():
    records = [
        {
            "date": "2026-04-01",
            "exercise": "bench_press",
            "weight": 185.0,
            "reps": 5,
        },
        {
            "date": "2026-04-02",
            "exercise": "bench_press",
            "weight": 190.0,
            "reps": 3,
        },
    ]

    summary = summarize_by_exercise(records)

    assert summary["bench_press"]["max_weight"] == 190.0
    assert summary["bench_press"]["average_weight"] == 187.5
    assert summary["bench_press"]["total_reps"] == 8
    assert summary["bench_press"]["total_volume"] == 1495.0


def test_summarize_by_exercise_two_exercises():
    records = [
        {
            "date": "2026-04-01",
            "exercise": "bench_press",
            "weight": 185.0,
            "reps": 5,
        },
        {
            "date": "2026-04-01",
            "exercise": "squat",
            "weight": 225.0,
            "reps": 5,
        },
    ]

    summary = summarize_by_exercise(records)

    assert summary["bench_press"]["max_weight"] == 185.0
    assert summary["bench_press"]["average_weight"] == 185.0
    assert summary["bench_press"]["total_reps"] == 5
    assert summary["bench_press"]["total_volume"] == 925.0

    assert summary["squat"]["max_weight"] == 225.0
    assert summary["squat"]["average_weight"] == 225.0
    assert summary["squat"]["total_reps"] == 5
    assert summary["squat"]["total_volume"] == 1125.0