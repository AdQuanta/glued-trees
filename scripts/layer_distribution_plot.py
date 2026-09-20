#%%
if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(Path(__file__).parents[1].__str__())

#%%
from matplotlib import pyplot as plt
from matplotlib.axes import Axes

from src.glued_trees import IndependentEdgeGluedTrees
from src.glued_trees.analyze import full_analysis
from src.glued_trees.visualize import plot_layer_distribution_board
from src.utils.visuals.matplotlib_support import draw_now, save_figure
from src.utils.visuals.matplotlib_support.mpl_types import Figure


def single_subplot(
    *,
    J_GT: float = 1.0,
    J_LR: float = 100.0,
    L: int = 5,
    p: float = 1.0,
    max_time: float = 100,
    dt: float = 0.1,
    W: float = 1.0,
    ax: Axes,
) -> None:
    graph = IndependentEdgeGluedTrees(
        L=L,
        J_GT=J_GT,
        J_LR=J_LR,
        p=p,
        add_path_edges=False,
        W=W,
        hamiltonian_convention="laplacian",
    )
    results = full_analysis(graph, max_t=max_time, dt=dt)
    plot_layer_distribution_board(
        results, ax=ax, color_scheme="Light-mode", colorbar="Add"
    )


def _pretty_figure(
    figure: Figure,
    axes: list[Axes],
    disorder_widths: list[float],
) -> None:
    figure.suptitle("Layer Distribution for Different Disorder Widths")
    for axis in axes[:-1]:
        axis.set_xlabel("")
        axis.set_xticks([])
    for axis, W in zip(axes, disorder_widths):
        axis.text(
            -0.22,
            0.5,
            f"$W={W}$",
            transform=axis.transAxes,
            fontsize=12,
            verticalalignment="center",
        )
    figure.tight_layout()


def main(disorder_widths: list[float] = [0.1, 1.0, 10.0]) -> None:
    figure, axes = plt.subplots(nrows=3, ncols=1)
    for index, W in enumerate(disorder_widths):
        single_subplot(W=W, ax=axes[index])
    _pretty_figure(figure, list(axes), disorder_widths)
    draw_now()
    save_figure(figure, file_name="layer_distribution", extensions=["png", "pdf"])


if __name__ == "__main__":
    main()
