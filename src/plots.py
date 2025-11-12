"""Plot helpers."""

import matplotlib.pyplot as plt


def save_hist(series, path):
    series.hist()
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
