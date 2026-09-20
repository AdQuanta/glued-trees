#%%
if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(Path(__file__).parents[1].__str__())

#%%
from typing import Generator, Literal

import numpy as np
from matplotlib import pyplot as plt

from src.glued_trees import IndependentEdgeGluedTrees
from src.glued_trees.analyze import full_analysis
from src.glued_trees.visualize import capture_tree_movie, full_movie_figure_frame_at_time
from src.utils.prints import ProgressBar
from src.utils.visuals.matplotlib_support import (
    new_figure,
    plot_with_spread,
    save_figure,
    twin_axis,
)
from src.utils.visuals.matplotlib_support.mpl_types import Figure


def capture_movie(
    J_GT: float = 1.0,
    J_LR: float = 1.0,
    L: int = 6,
    p: float = 0.6,
    W: float = 1.0,
    max_time: float = 60,
    dt: float = 0.1,
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
    full_movie_figure_frame_at_time(results, t="Final")
    capture_tree_movie(results, fps=30.0)


def _capture_frame(
    *,
    J_GT: float = 1.0,
    J_LR: float = 1.0,
    L: int = 5,
    p: float = 1.0,
    W: float = 1.0,
    max_time: float = 1000,
    dt: float = 0.1,
) -> Figure:
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
    data = full_movie_figure_frame_at_time(results, t="Final")
    figure = data["fig"]
    figure_name = f"final_frame_{data['movie_title_str']}".replace(":", "")
    save_figure(figure, figure_name, extensions=["png"])
    return figure


def _kwargs_gen(
    parameter_name: str | None, values: list[float] | np.ndarray
) -> Generator[dict[str, float], None, None]:
    if parameter_name is None:
        yield {}
    else:
        for value in values:
            yield {parameter_name: value}


coupling_values = np.linspace(0.0001, 20, 51)
num_repeats = 20
max_time = 100


def capture_frames(
    parameter_name: str | None = "J_GT",
    values: list[float] | np.ndarray = coupling_values,
) -> None:
    for kwargs in _kwargs_gen(parameter_name, values):
        figure = _capture_frame(**kwargs)
        plt.close(figure)


def _compute_center_frequency(
    frequency_vector: np.ndarray, frequency_response: np.ndarray
) -> float:
    magnitude_squared = np.abs(frequency_response) ** 2
    return np.sum(frequency_vector * magnitude_squared) / np.sum(magnitude_squared)


def _compute_average_value(
    time_vector: np.ndarray,
    exit_probabilities: np.ndarray,
    method: Literal["simple", "trapezoidal"] = "simple",
) -> float:
    if method == "simple":
        return float(np.mean(exit_probabilities))
    if method == "trapezoidal":
        return float(
            np.trapezoid(exit_probabilities, time_vector)
            / (time_vector[-1] - time_vector[0])
        )
    raise ValueError(f"Unknown method: {method!r}. Use 'simple' or 'trapezoidal'.")


def _extract_results(
    *,
    J_GT: float = 1.0,
    J_LR: float = 1.0,
    L: int = 5,
    p: float = 1.0,
    W: float = 1.0,
    max_time: float = max_time,
    dt: float = 0.05,
    rng: int = 0,
) -> tuple[float, float]:
    graph = IndependentEdgeGluedTrees(
        L=L,
        J_GT=J_GT,
        J_LR=J_LR,
        p=p,
        add_path_edges=False,
        W=W,
        hamiltonian_convention="laplacian",
        rng=rng,
    )
    results = full_analysis(graph, max_t=max_time, dt=dt, prog_bar=False)
    frequency_vector, frequency_response = results.exit_probability_fourier_transform()
    return (
        _compute_center_frequency(frequency_vector, frequency_response),
        _compute_average_value(results.times, results.exit_probabilities),
    )


def _add_item_to_dict_of_lists(
    values_by_parameter: dict[float, list[float]], key: float, value: float
) -> None:
    values_by_parameter.setdefault(key, []).append(value)


def plot_mean_frequency(
    parameter_name: str | None = "J_GT",
    values: list[float] | np.ndarray = coupling_values,
    num_repeats: int = num_repeats,
) -> None:
    frequencies: dict[float, list[float]] = {}
    probabilities: dict[float, list[float]] = {}
    progress = ProgressBar(num_repeats * len(values), print_length=80)
    for kwargs in _kwargs_gen(parameter_name, values):
        for rng in range(num_repeats):
            parameter_value = kwargs[parameter_name]
            kwargs["rng"] = rng
            progress.next(extra_str=f"Computing center frequency for {kwargs}")
            center_frequency, average_probability = _extract_results(**kwargs)
            _add_item_to_dict_of_lists(frequencies, parameter_value, center_frequency)
            _add_item_to_dict_of_lists(probabilities, parameter_value, average_probability)

    _, frequency_axis = new_figure()
    probability_axis = twin_axis(frequency_axis)
    plot_with_spread(x_y_values_dict=frequencies, axes=frequency_axis, color="tab:blue")
    plot_with_spread(x_y_values_dict=probabilities, axes=probability_axis, color="tab:red")
    frequency_axis.set_xlabel(parameter_name)
    frequency_axis.set_ylabel("Center Frequency [Hz]")
    probability_axis.set_ylabel("Mean Exit Probability")
    probability_axis.set_title("Independent-Edge Glued Trees\nMean Center Frequency and Exit Probability")
    save_figure(file_name="mean_frequency_plot", extensions=["png", "svg", "pdf"])
    progress.clear()


def main() -> None:
    capture_frames()


if __name__ == "__main__":
    main()
