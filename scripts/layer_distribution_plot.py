#%%
if __name__ == "__main__":
    import sys
    from pathlib import Path
    # Add the parent directory to the system path
    sys.path.append(
        Path(__file__).parents[1].__str__()
    )

#%% 
import numpy as np
from typing import Generator, Literal


from src.glued_trees import GluedTreesSmallWorld
from src.glued_trees.visualize import plot_layer_distribution_board
from src.glued_trees.analyze import full_analysis

from src.utils.visuals.matplotlib_support import draw_now, save_figure, close_all, plot_with_spread, new_figure, twin_axis
from src.utils.visuals.matplotlib_support.mpl_types import Figure
from src.utils.prints import ProgressBar


from matplotlib import pyplot as plt    
from matplotlib.axes import Axes 



def single_subplot(
    *,
    J = -1.0,        # Coupling strength   # -1.0 it first attemps
    J2 = -100,       # All-to-all coupling strength
    h = 5,           # Tree height
    p = 1,           # Small-world connection probability
    max_time=100,    # Maximum time for the simulation
    dt=0.1,          # Time step for the simulation
    sigma = 1.0,     # Disorder strength
    ax:Axes
) -> Figure:
    
    ## Compute glued-trees state:
    gt = GluedTreesSmallWorld(h, J, J2, p, False, sigma, distribution="gaussian")
    res = full_analysis(gt, max_t=max_time, dt=dt)
    plot_layer_distribution_board(res, ax=ax, color_scheme="Light-mode", colorbar="Add")


def _pretty_figure(
    fig:Figure, 
    axes:list[Axes],
    sigma_values: list[float]
) -> None:
    fig.suptitle("Layer Distribution for Different Disorder Strengths")
    ## remove x-axis lables and ticks for top 2 axes:
    for ax in axes[:-1]:
        ax.set_xlabel("")
        ax.set_xticks([])

    ## Put the sigma values in the right side of the subplots:
    for ax, sigma in zip(axes, sigma_values):
        ax.text(-0.22, 0.5, f"$\\sigma={sigma}$", transform=ax.transAxes, fontsize=12,
                verticalalignment="center")

    ## Finally:
    fig.tight_layout()

    print("Done prettying up the figure.")


def main(
    sigma_values: list[float] = [0.1, 1.0, 10.0]
):

    fig, (axes) = plt.subplots(nrows=3, ncols=1) 
    for i, sigma in enumerate(sigma_values):
        ax = axes[i]
        single_subplot(sigma=sigma, ax=ax)
    
    _pretty_figure(fig, axes, sigma_values)

    draw_now()
    save_figure(fig, file_name="layer_distribution", extensions=["png", "pdf"])


if __name__ == "__main__":
    main()


