# for type hints:
from typing import Optional, cast, TypeAlias, TypeVar

# For saving plots:
from pathlib import Path
import os
import time

## Import matplotlib:
import matplotlib as mpl
try:
    mpl.use('TkAgg')
except ImportError as e:
    import warnings
    warnings.warn(str(e))

import matplotlib.pyplot as plt
plt.ion()

from .mpl_types import *


# Use our other utils 
from ... import strings, files
from ....code_paths import outputs

## select the proper backend for rendering figures: 
import warnings

import numpy as np

## Types:
_Numeric = TypeVar("_Numeric", int, float)
PlotWithSpreadReturnValue : TypeAlias = list[Line2D]



def turn_latex_on(value:bool = True) -> None:
    plt.rcParams['text.usetex'] = value


def get_saved_figures_folder()->Path:
    figures_folder = outputs / "figures"
    files.force_folder_exists(figures_folder)
    return figures_folder


def save_figure(fig:Optional[Figure]=None, file_name:Optional[str]=None, extensions:list[str]=["png", "svg"]) -> None:
    # Figure:
    if fig is None:
        fig = plt.gcf()
    # Title:
    if file_name is None:
        file_name = strings.time_stamp()
    # Figures folder:
    folder = get_saved_figures_folder()
    # Full path:
    fullpath = folder.joinpath(file_name)
    fullpath_str = str(fullpath.resolve())
    # Add extensions
    for ext in extensions:
        if fullpath_str.endswith(ext):            
            fullpath_str_with_ext = fullpath_str
        else:
            fullpath_str_with_ext = fullpath_str+"."+ext
        # Save:
        fig.savefig(fullpath_str_with_ext)
    return 


def save_all_figures(extensions:list[str]=["png"]) -> None:
    time_stamp = strings.time_stamp()
    for i in plt.get_fignums():
        fig = plt.figure(i)
        name = time_stamp + f"_{i}"
        save_figure(fig, file_name=name, extensions=extensions)


def new_figure() -> tuple[Figure, Axes]:
    fig, (ax) = plt.subplots(nrows=1, ncols=1) 
    return fig, ax


def close_all():
    plt.close('all')


def draw_now():
    assert plt.isinteractive()  # Check if interactive mode is on

    sleep_time: float = 0.01
    time.sleep(sleep_time)
    plt.pause(sleep_time)
    time.sleep(sleep_time)


def no_y_axis_offset(ax:Axes) -> None:
    ax.yaxis.set_major_formatter(ScalarFormatter(useOffset=False))


def twin_axis(axis:Axes) -> Axes:
    twin = axis.twinx()
    for ax, color in zip([axis, twin], ["tab:blue", "tab:red"], strict=True):
        ax.set_ylabel(ax.get_ylabel(), color=color)
        ax.tick_params(axis='y', labelcolor=color)
    plt.sca(twin)
    return twin


def _xs_and_ys_to_values_dict(x_vals:list[_Numeric], y_vals:list[_Numeric]) -> dict[_Numeric, list[_Numeric]]:
    x_y_values_dict : dict[_Numeric, list[_Numeric]] = {}
    for x, y in zip(x_vals, y_vals, strict=True):
        if x in x_y_values_dict:
            x_y_values_dict[x].append(y)
        else:
            x_y_values_dict[x] = [y]
    return x_y_values_dict


def plot_with_spread(
    x_y_values_dict:dict[_Numeric, list[_Numeric]]|None=None, 
    x_vals:list[_Numeric]|None=None, 
    y_vals:list[_Numeric]|None=None, 
    also_plot_max_min_dots:bool=True,
    axes:Axes|None=None,
    disable_spread:bool=False,
    **plt_kwargs
) -> PlotWithSpreadReturnValue:
    ## Check inputs:
    if x_y_values_dict is None:
        assert x_vals is not None
        assert y_vals is not None
        x_y_values_dict = _xs_and_ys_to_values_dict(x_vals, y_vals)
    else:
        assert x_vals is None
        assert y_vals is None

    if axes is None:
        fig = plt.figure()
        axes = fig.add_subplot(1,1,1)

    # Convert y_values_matrix to a NumPy array for easier manipulation
    y_means = []
    y_stds  = []
    y_maxs  = []
    y_mins  = []
    x_values = sorted(list(x_y_values_dict.keys()))
    for x in x_values:
        y_values = x_y_values_dict[x]
        y_values = np.array(y_values)

        # Calculate the mean and standard deviation along the 1st axis (columns)
        y_means.append(np.mean(y_values))
        y_stds.append(np.std(y_values))
        y_maxs.append(max(y_values))
        y_mins.append(min(y_values))
    
    # Plotting the mean values
    lines = axes.plot(x_values, y_means, **plt_kwargs)
    color = lines[0].get_color()
    
    if disable_spread:
        return lines

    # Adding a shaded region to represent the spread (1 standard deviation here)
    y_means = np.array(y_means)
    y_stds = np.array(y_stds)
    fill = axes.fill_between(x_values, y_means - y_stds, y_means + y_stds, color=color, alpha=0.2)
    lines.append(fill)

    # Add max-min lines:
    if also_plot_max_min_dots:
        maxs = axes.plot(x_values, y_maxs, ":", color=color)
        mins = axes.plot(x_values, y_mins, ":", color=color)

        lines.append(maxs)
        lines.append(mins)

    return lines