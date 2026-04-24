from workout_tracker.report import (
    summarize_exercise, 
    summarize_all,
    summarize_personal_records,
    summarize_total_volume,
)


def test_summarize_exercise():
    """Test that summarize_exercise formats one exercise correctly."""
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
    """Test that summarize_all formats all exercises correctly."""
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


def test_summarize_total_volume():
    """Test that total volume is formatted correctly."""
    result = summarize_total_volume(3425.0)
    assert result == "Total workout volume: 3425.0"


def test_summarize_personal_records():
    """Test that personal records are formatted correctly."""
    personal_records = {
        "bench_press": 190.0,
        "squat": 225.0,
    }
    result = summarize_personal_records(personal_records)
    assert "Personal Records" in result
    assert "bench_press: 190.0" in result
    assert "squat: 225.0" in result