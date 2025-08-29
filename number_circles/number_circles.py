import matplotlib.pyplot as plt
import numpy as np


def plot_number_circles(max_n=27, outfile=None, dpi=100):
    """
    Generate a grid of number circle plots.
    Args:
            max_n (int): Maximum number to consider (inclusive).
            outfile (str or None): Path to save the output image. If None, does not save.
    """
    plots = []
    for i in range(2, max_n + 1):
        for j in range(1, max_n):
            if i > j + (i / 2):
                plots.append((i, j))

    ncols = int(np.ceil(np.sqrt(len(plots))))
    nrows = int(np.ceil(len(plots) / ncols))

    fig, axes = plt.subplots(
        nrows=nrows, ncols=ncols, figsize=(12, 12), sharex=True, sharey=True
    )
    axes = np.array(axes).flatten()

    for idx, (i, j) in enumerate(plots):
        ax = axes[idx]
        angles = np.linspace(0, 2 * np.pi, i, endpoint=False)
        x = np.sin(angles)
        y = np.cos(angles)

        ax.plot(x, y, "o", markersize=2, color="k")

        circle = plt.Circle((0, 0), 1, color="lightgray", fill=False, alpha=0.5)
        ax.add_artist(circle)

        visited = set()
        current = 0
        for _ in range(i):
            next_point = (current + j) % i
            if (current, next_point) in visited or (next_point, current) in visited:
                break
            ax.plot(
                [x[current], x[next_point]],
                [y[current], y[next_point]],
                "k-",
                lw=1,
                alpha=0.5,
            )
            visited.add((current, next_point))
            current = next_point
            if current == 0:
                break

        ax.set_aspect("equal")
        ax.axis("off")

    for ax in axes[len(plots) :]:
        ax.axis("off")

    plt.tight_layout()
    if outfile:
        plt.savefig(outfile, dpi=dpi)
    plt.show()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Plot number circles grid.")
    parser.add_argument(
        "--max_n", type=int, default=20, help="Maximum number to consider (inclusive)"
    )
    parser.add_argument(
        "--outfile", type=str, default=None, help="Output image file path (optional)"
    )
    parser.add_argument(
        "--dpi", type=int, default=100, help="DPI for saving the image (default: 100)"
    )
    args = parser.parse_args()
    plot_number_circles(max_n=args.max_n, outfile=args.outfile)
