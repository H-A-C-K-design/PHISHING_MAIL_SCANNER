import matplotlib.pyplot as plt


def save_plot(path, figure):
    figure.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(figure)
