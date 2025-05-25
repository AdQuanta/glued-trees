# for type hints:
from typing import Optional

# For saving plots:
from pathlib import Path
import os
import time

## Import matplotlib:
import matplotlib.pyplot as plt
import matplotlib as mpl

from .mpl_types import *


# Use our other utils 
from ... import strings, assertions, arguments, types, prints, lists
from ....code_paths import outputs

## select the proper backend for rendering figures: 
try:
    mpl.use('TkAgg')

except ImportError as e:
    import warnings
    warnings.warn(str(e))

plt.ion()


def turn_latex_on(value:bool = True) -> None:
    plt.rcParams['text.usetex'] = value


def get_saved_figures_folder()->Path:
    figures_folder = outputs / "figures"
    if not figures_folder.is_dir():
        os.mkdir(str(figures_folder.resolve()))
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