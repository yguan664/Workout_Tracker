import pytest
from workout_tracker.io import load_workouts


def test_load_workouts(tmp_path):
    """Test that load_workouts reads a CSV and returns correct data."""
    f = tmp_path / "workouts.csv"
    f.write_text(
        "date,exercise,weight,reps\n"
        "2026-04-01,bench_press,185,5\n"
    )
    result = load_workouts(str(f))
    assert result == [
        {
            "date": "2026-04-01",
            "exercise": "bench_press",
            "weight": 185.0,
            "reps": 5,
        }
    ]


def test_bad_weight(tmp_path):
    """Test that negative weight raises ValueError."""
    f = tmp_path / "bad.csv"
    f.write_text("date,exercise,weight,reps\n2026-04-01,squat,-10,5\n")
    with pytest.raises(ValueError):
        load_workouts(str(f))


def test_bad_reps(tmp_path):
    """Test that zero reps raises ValueError."""
    f = tmp_path / "bad.csv"
    f.write_text("date,exercise,weight,reps\n2026-04-01,squat,100,0\n")
    with pytest.raises(ValueError):
        load_workouts(str(f))
