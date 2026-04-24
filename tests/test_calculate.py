from workout_tracker.calculate import (
    calculate_total_volume,
    calculate_volume,
    filter_by_exercise,
    get_personal_records,
    summarize_by_exercise,
)


def test_calculate_volume():
    """Test simple volume calculation"""
    record = {
        "date": "2026-04-01",
        "exercise": "bench_press",
        "weight": 185.0,
        "reps": 5,
    }

    assert calculate_volume(record) == 925.0


def test_summarize_by_exercise_one_exercise():
    """Test summary for one exercise"""
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
    """Test summary for multiple exercises"""
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


def test_calculate_total_volume():
    """Test total volume over records"""
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

    assert calculate_total_volume(records) == 2050.0


def test_filter_by_exercise():
    """Test filtering records by exercise"""
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

    result = filter_by_exercise(records, "bench_press")

    assert len(result) == 1
    assert result[0]["exercise"] == "bench_press"


def test_get_personal_records():
    """Test max weight per exercise"""
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
        {
            "date": "2026-04-01",
            "exercise": "squat",
            "weight": 225.0,
            "reps": 5,
        },
    ]

    result = get_personal_records(records)

    assert result["bench_press"] == 190.0
    assert result["squat"] == 225.0