import os
import pytest
from workout_tracker.io import load_workouts


def test_load_workouts():
    path = os.path.join("data", "sample_workouts.csv")
    result = load_workouts(path)

    assert len(result) > 0
    for row in result:
        assert "date" in row
        assert "exercise" in row
        assert "weight" in row
        assert "reps" in row
        assert isinstance(row["date"], str)
        assert isinstance(row["exercise"], str)
        assert isinstance(row["weight"], float)
        assert isinstance(row["reps"], int)

def test_bad_weight(tmp_path):
    f = tmp_path / "bad.csv"
    f.write_text("date,exercise,weight,reps\n2026-04-01,squat,-10,5\n")
    with pytest.raises(ValueError):
        load_workouts(str(f))


def test_bad_reps(tmp_path):
    f = tmp_path / "bad.csv"
    f.write_text("date,exercise,weight,reps\n2026-04-01,squat,100,0\n")
    with pytest.raises(ValueError):
        load_workouts(str(f))
