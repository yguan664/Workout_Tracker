from workout_tracker.report import summarize_exercise, summarize_all


def test_summarize_exercise():
    stats = {
        "max_weight": 190.0,
        "average_weight": 186.7,
        "total_reps": 13,
        "total_volume": 2427.0,
    }
    result = summarize_exercise("bench_press", stats)
    assert "bench_press" in result
    assert "190.0" in result
    assert "186.7" in result
    assert "13" in result
    assert "2427.0" in result


def test_summarize_all():
    all_stats = {
        "bench_press": {
            "max_weight": 190.0,
            "average_weight": 186.7,
            "total_reps": 13,
            "total_volume": 2427.0,
        },
        "squat": {
            "max_weight": 235.0,
            "average_weight": 230.0,
            "total_reps": 8,
            "total_volume": 1845.0,
        },
    }
    result = summarize_all(all_stats)
    assert "bench_press" in result
    assert "squat" in result