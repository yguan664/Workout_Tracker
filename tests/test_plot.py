from workout_tracker.plot import plot_total_volume


def test_plot_total_volume(tmp_path):
    """Test plot total volume."""
    stats = {
        "bench_press": {"total_volume": 2420.0},
        "squat": {"total_volume": 1830.0},
    }

    output = tmp_path / "volume.png"
    plot_total_volume(stats, str(output))

    assert output.exists()