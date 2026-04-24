import matplotlib.pyplot as plt


def plot_total_volume(stats, output_path):
    """Plot total volume by exercise."""
    exercises = []
    volumes = []

    for exercise in stats:
        exercises.append(exercise)
        volumes.append(stats[exercise]["total_volume"])

    plt.figure()
    plt.bar(exercises, volumes)
    plt.xlabel("Exercise")
    plt.ylabel("Total Volume")
    plt.title("Total Volume by Exercise")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()