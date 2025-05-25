from typing import TypedDict, Callable, Final

## Glued Trees imports:
from .classes import GluedTrees
from .analyze import FullAnalysisResults, TimeEvolutionResultsType

## Our common utils
from ..utils.prints import ProgressBar
from ..utils.visuals.matplotlib_support.mpl_types import Axes, Figure
from ..utils.visuals.videos import VideoRecorder

## For graphics:
from matplotlib import pyplot as plt
import matplotlib

# For graphics in vscode:
matplotlib.use('TkAgg')
plt.ion()  # Turn on interactive mode
# Set default plot parameters
plt.rcParams["font.size"] = 12
plt.rcParams["font.sans-serif"] = "Arial"

## Math:
import numpy as np
from numpy.typing import NDArray

## For sleep and cleanup:
from time import sleep
from gc import collect as gc_collect
import threading


FULL_GARBAGE_COLLECTION_INTERVAL : Final[int] = 100
MAX_FLOAT_STR_DECIMALS : Final[int] = 3


## ================================================ ##
#                 Global Functions                   #


def plot_layer_distribution_stairs(
    gt: GluedTrees, res: TimeEvolutionResultsType,
    up_to_time:float|None = None,
    ax:Axes|None = None, # Optional: pass an existing axis to plot on
) -> Axes:
    
    ## Times: 
    times = _common_get_times_array(res, up_to_time)

    # Visualize layer distribution over time
    cmap = plt.get_cmap("rainbow")
    norm = plt.Normalize(vmin=times[0], vmax=times[-1])
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    def _per_time_function(t_ind:int, t:float, layer_distribution:np.ndarray, ax:Axes) -> None:
        color = cmap(norm(t))
        ax.stairs(
            layer_distribution,
            np.arange(gt.num_layers + 1),
            color=color,
            fill=True,
            alpha=0.8,
        )

    ax = _common_plot_layer_distribution(
        gt=gt, res=res, times=times,
        _per_time_function=_per_time_function, 
        up_to_time=up_to_time, ax=ax
    )

    ax.set_xlabel("Layer index")
    ax.set_ylabel("Population")
    ax.tick_params(axis="both", which="major")
    plt.tight_layout()

    # Add colorbar for time
    cbar = ax.figure.colorbar(sm, ax=ax, pad=0.02)
    cbar.set_label("Time")

    return ax


def plot_layer_distribution_board(
    res:FullAnalysisResults,
    up_to_time:float|None = None,
    flip_y_axis:bool = True,
    ax:Axes|None = None, # Optional: pass an existing axis to plot on
) -> Axes:
    
    gt = res.glued_trees

    ## Times:
    times = _common_get_times_array(res, up_to_time)

    ## Axes:
    ax = _complete_axes_if_missing(ax)
    # x and y axis create a checkerboard pattern where:
    # x axis is for the number of times
    # y axis if for the number of layers
    x_len = len(times) 
    y_len = gt.num_layers
    x = np.arange(x_len+1)
    y = np.arange(y_len+1)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros((y_len, x_len))

    def j_index(layer_index:int) -> int:
        """
        Get the j index for the layer index.
        """
        if flip_y_axis:
            return y_len - layer_index - 1
        else:
            return layer_index

    ## Call common plot function:
    def _per_time_function(t_ind:int, t:float, layer_distribution:np.ndarray, ax:Axes) -> None:
        ## If i is the time inext and j is the layer index, then: 
        # Fill the chacker board such that the intensity (alpha value) of the square at position (i, j) 
        # is the value of the layer distribution at that time and layer index:
        i = t_ind
        for layer_index, dist in enumerate(layer_distribution):
            # j is the layer index in reversed order for a plot that looks like the tree:
            j = j_index(layer_index)
            Z[j, i] = dist

    ax = _common_plot_layer_distribution(
        gt=gt, res=res, times=times,
        _per_time_function=_per_time_function, 
        up_to_time=up_to_time,
        ax=ax
    )

    ## use the mesh Z to create a board:
    ax.pcolormesh(X, Y, Z, shading='flat', cmap='inferno', alpha=1, vmin=0, vmax=1)
    ax.set_xlabel("time")
    ax.set_ylabel("Layer")

    ## Update the x-ticks:
    old_xticks = ax.get_xticks()
    new_xticks, new_indices_to_use = _fix_board_ticks(old_xticks, acossiated_values=times)
    new_xticks_labels = [f"{times[i]}" for i in new_indices_to_use]
    ax.set_xticks(new_xticks)
    ax.set_xticklabels(new_xticks_labels)

    ## Reverse the y-axis:
    old_yticks = ax.get_yticks()
    new_yticks, new_indices_to_use = _fix_board_ticks(old_yticks, acossiated_values=y)
    if new_yticks[-1] > y[-1]:
        new_yticks.pop(-1)
        new_indices_to_use.pop(-1)
    new_yticks_labels = [f"{j_index(j)}" for j in new_indices_to_use]
    ax.set_yticks(new_yticks)
    ax.set_yticklabels(new_yticks_labels)

    return ax


def plot_exit_probability(res:FullAnalysisResults, up_to_time:float, 
    ax:Axes|None = None
) -> Axes:
    """
    Plot the exit probability as a function of time.
    """
    ax = _complete_axes_if_missing(ax)

    times = _common_get_times_array(res, up_to_time)

    # Get the exit probability
    exit_prob = res.exit_probabilities[:len(times)]

    # Plot the exit probability
    lines = ax.plot(times, exit_prob, label="Exit Probability", color='tab:blue')
    if len(times) < 10:
        lines[0].set_marker('o')
    ax.set_xlabel("Time")
    ax.set_ylabel("Exit Probability")
    # ax.grid()

    # Set x-axis limits
    if up_to_time is not None:
        ax.set_xlim(0, up_to_time)

    return ax


def plot_spectrum(
    gt: GluedTrees, res: TimeEvolutionResultsType,
    ax:Axes|None = None, # Optional: pass an existing axis to plot on
) -> Axes:
    """
    Plot the spectrum of the system.
    """
    ax = _complete_axes_if_missing(ax)

    gt.plot_spectrum()

    return ax


def draw_now():
    """
    Draw the current figure and pause for a short time.
    """
    plt.show()
    plt.pause(0.001)


def capture_tree_movie(
    res: FullAnalysisResults, 
    fps: float = 10.0, 
) -> str:
    
    ## pramaters to help with stable movie strings:
    movie_helper_data = _get_movie_helper_data(res)

    ## for each time, create a figure and draw the trees:
    with VideoRecorder(fps=fps) as recorder:
        for t in ProgressBar(res.times, print_prefix="Rendering frames"):
            fig = _full_movie_figure_frame_at_time(t, res, movie_helper_data)
            recorder.capture(fig)
            movie_helper_data = _movie_cleanup(fig, movie_helper_data)
            

    ## Return the path to the video:
    return recorder.video_path
    

def plot_tree_at_time(
    res:FullAnalysisResults, time:float,
    ax:Axes|None = None, # Optional: pass an existing axis to plot on
    _auto_apply_title:bool = True,
) -> Axes:
    """ 
    Plot the trees at a given time.
    Parameters
    ----------      
    res : Result
        The result of the time evolution.
    time : float
        The time at which to plot the trees.
    """
    gt = res.glued_trees
    ax = _complete_axes_if_missing(ax)

    ## Find the index of the time closest to the given time
    times = np.array(res.times)
    idx = np.argmin(np.abs(times - time))
    time = res.times[idx]
    # Get the state at that time
    gt.plot_graph_on_ax(ax, res.states[idx].full()[:, 0])

    if _auto_apply_title:
        ax.set_title(f"t = {time:.1f}")

    return ax


def _complete_axes_if_missing(ax:Axes|None) -> Axes:
    if ax is None:
        fig, ax = plt.subplots(1, 1)
    return ax




## =============================================== ##
#                     Helpers                       # 

class AxesDict(TypedDict):
    trees: Axes
    layer_distribution: Axes
    exit_probablity: Axes


def _create_empty_movie_frame_figure() -> tuple[Figure, AxesDict]:
    """
    Create the figure according to the following layout:
    1. On the left: a big subplot where the trees will be drawn (ax1)
    2. On the right upper corner: the layer distribution will be drawn over time (ax2)
    3. On the right lower corner: a more narrow subplot, where the exit-probability alone will be drawn as a function of time (ax3)
    Layout:
    +-------------------+----------------------+
    |                   |         ax2          |
    |       ax1         |----------------------|
    |                   |         ax3          |
    +-------------------+----------------------+
    """
    fig = plt.figure(figsize=(12, 6))
    # Use GridSpec to create the desired layout
    gs = fig.add_gridspec(2, 2, width_ratios=[1, 2], height_ratios=[3, 1.2])

    # ax1: left, spans both rows
    ax1 = fig.add_subplot(gs[:, 0])
    # ax2: top right
    ax2 = fig.add_subplot(gs[0, 1])
    # No x-axis for ax2:
    # ax2.xaxis.set_visible(False)

    # ax3: bottom right
    ax3 = fig.add_subplot(gs[1, 1])

    fig.subplots_adjust(wspace=0.2, hspace=0.15)
    axes = AxesDict(
        trees=ax1,
        layer_distribution=ax2,
        exit_probablity=ax3,
    )

    return fig, axes

def _parameters_str(parameters:dict) -> str:
    """
    Convert the parameters to a string for display.
    """
    params_str = ", ".join([f"{key}: {parameters[key]}" for key in ["h", "J"]])
    return params_str


def _add_titles(fig:Figure, res:FullAnalysisResults, t:float, movie_helper_data:dict) -> None:
    ## Unpack helper data:
    end_time            = movie_helper_data["end_time"]
    max_time_str_len    = movie_helper_data["max_time_str_len"]
    max_left_digits     = movie_helper_data["max_left_digits"]
    max_right_digits    = movie_helper_data["max_right_digits"]    

    ## Create the supre_titles:
    # Format time with fixed width and decimals for stable title
    time_str_frmt = lambda val: f"{val:>{max_left_digits + max_right_digits + 1}.{max_right_digits}f}"
    time_str = f"time = {time_str_frmt(t)} / {time_str_frmt(end_time)}"
    fig.supxlabel(time_str, fontsize=16)
    # Title with parameters:
    fig.suptitle("Glued Trees", fontsize=20, y=0.98)
    fig.text(0.5, 0.92, _parameters_str(res.parameters), ha='center', va='top', fontsize=12)


def _full_movie_figure_frame_at_time(
    t:float, res:FullAnalysisResults, 
    movie_helper_data:dict,
) -> Figure:
    
    ## Create the figure with subplots axes according to the layout:        
    fig, axes = _create_empty_movie_frame_figure()
    _add_titles(fig, res, t, movie_helper_data)

    ## Plot each of the subplots:
    # Plot the tree:
    plot_tree_at_time(res, t, ax=axes['trees'], _auto_apply_title=False)
    # Plot the layer distribution:
    plot_layer_distribution_board(res, up_to_time=t, ax=axes['layer_distribution'])
    # Plot the exit probability:
    plot_exit_probability(res, up_to_time=t, ax=axes['exit_probablity'])

    # return fig
    return fig
    

def _get_movie_helper_data(res: FullAnalysisResults) -> dict:
    ## Get information about simulation times:
    times = res.times
    max_time_str_len = max(len(str(t)) for t in times)
    end_time = times[-1]

    # Determine max digits to the left and right of the decimal point
    max_left_digits = 0
    max_right_digits = 0
    for t in times:
        s = str(t)

        if "." in s:
            left, right = s.split(".")
        else:
            left, right = s, ""

        if len(right) > MAX_FLOAT_STR_DECIMALS:
            right = right[:MAX_FLOAT_STR_DECIMALS]

        max_left_digits = max(max_left_digits, len(left)) 
        max_right_digits = max(max_right_digits, len(right))


    # Compile into a single dict:
    data = {
        "end_time": end_time,
        "max_time_str_len": max_time_str_len,
        "max_left_digits": max_left_digits,
        "max_right_digits": max_right_digits,
        "frames_counter": 0,  # Counter for frames captured
    }
    return data


def _movie_cleanup(fig:Figure, movie_helper_data:dict) -> dict:
    plt.close(fig)  # Close the figure to free memory
    if movie_helper_data['frames_counter'] >= FULL_GARBAGE_COLLECTION_INTERVAL:
        # If we have captured more than 100 frames, reset the counter
        movie_helper_data['frames_counter'] = 0
        gc_collect()  # Collect garbage to free memory
        sleep(1)  # Sleep to allow the system to catch up
    else:
        movie_helper_data['frames_counter'] += 1
    return movie_helper_data


def _common_plot_layer_distribution(
    gt: GluedTrees, res: TimeEvolutionResultsType,
    times:list[float],
    _per_time_function:Callable[[int, float, np.ndarray, Axes], None], 
    up_to_time:float|None = None,
    ax:Axes|None = None, # Optional: pass an existing axis to plot on
) -> Axes:
    
    ## Complete parameters:
    ax = _complete_axes_if_missing(ax)
    fig = ax.figure
    if up_to_time is None:
        up_to_time = res.times[-1]


    for idx, t in enumerate(res.times):
        # Skip t not in times:
        if t not in times:
            continue

        layer_distribution = gt.get_layer_distribution(res.states[idx])
        _per_time_function(idx, t, layer_distribution, ax)

    return ax


def _common_get_times_array(res, up_to_time:float|None) -> list[float]:
    """
    Get the times array for the given time evolution results up to a given time.
    """
    ## Since res.times is sorted, efficiently select all times up to up_to_time
    end_time = up_to_time if up_to_time is not None else res.times[-1]
    return [t for t in res.times if t <= end_time]


def _fix_board_ticks(old_ticks:np.ndarray, acossiated_values:np.ndarray|list[float]) -> tuple[list[float], list[int]]:
    new_ticks = []
    new_indices_to_use = []
    for x in old_ticks:
        if int(round(x)) != x:
            continue
        if x >= len(acossiated_values):
            continue
        if x < 0:
            raise ValueError(f"X tick {x} is out of range")
        new_indices_to_use.append(int(x))
        new_ticks.append(x+0.5)    
    return new_ticks, new_indices_to_use

