import matplotlib.pyplot as plt

plt.rcParams.update({
    "figure.figsize": (8,5),
    "axes.grid": True, "grid.alpha": 0.25,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.titlesize": 14, "axes.labelsize": 12
})

def savefig(path: str):
    plt.tight_layout()
    plt.savefig(path, dpi=180)
