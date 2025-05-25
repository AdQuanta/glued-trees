if __name__ == "__main__":
    import sys
    from pathlib import Path
    # Add the parent directory to the system path
    sys.path.append(
        Path(__file__).parents[1].__str__()
    )


from src.glued_trees import GluedTreesSmallWorld
from src.glued_trees.visualize import plot_tree_at_time, plot_layer_distribution_stairs, plot_layer_distribution_board, capture_tree_movie, draw_now
from src.glued_trees.analyze import full_analysis


def main(
    J = -1.,        # Coupling strength
    J2 = -1.,       # All-to-all coupling strength
    p = 1.,         # Small-world connection probability
    sigma = 1.,     # Disorder strength
    max_time=80,    # Maximum time for the simulation
    dt=0.05,           # Time step for the simulation
):
    
    ## Compute glued-trees state:
    gt = GluedTreesSmallWorld(4, J, p, False, sigma, distribution="gaussian")
    res = full_analysis(gt, max_t=max_time, dt=dt)

    # plot_layer_distribution_stairs(gt, res.time_evolution_results, up_to_time=40.0)
    # plot_layer_distribution_board(gt, res.time_evolution_results, up_to_time=40.0)

    # capture movie:
    capture_tree_movie(res, fps=30.0)

    pass


if __name__ == "__main__":
    main()
