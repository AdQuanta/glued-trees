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
from src.glued_trees.visualize import plot_tree_at_time, plot_layer_distribution_stairs, plot_layer_distribution_board
from src.glued_trees.visualize import capture_tree_movie, full_movie_figure_frame_at_time
from src.glued_trees.analyze import full_analysis

from src.utils.visuals.matplotlib_support import draw_now, save_figure, close_all, plot_with_spread, new_figure, twin_axis
from src.utils.visuals.matplotlib_support.mpl_types import Figure
from src.utils.prints import ProgressBar


from matplotlib import pyplot as plt    


def capture_movie(
    J = -1.0,        # Coupling strength   # -1.0 it first attemps
    J2 = -1.,       # All-to-all coupling strength
    h = 6,          # Tree height
    p = 0.6,         # Small-world connection probability
    sigma = 1.0,     # Disorder strength
    max_time=60,    # Maximum time for the simulation
    dt=0.1,           # Time step for the simulation
):
    
    ## Compute glued-trees state:
    gt = GluedTreesSmallWorld(h, J, p, False, sigma, distribution="gaussian")
    res = full_analysis(gt, max_t=max_time, dt=dt)
    data = full_movie_figure_frame_at_time(res, t="Final")

    # plot_layer_distribution_stairs(gt, res.time_evolution_results, up_to_time=40.0)
    # plot_layer_distribution_board(gt, res.time_evolution_results, up_to_time=40.0)

    # capture movie:
    capture_tree_movie(res, fps=30.0)

    pass






def _capture_frame(
    *,
    J = -1.0,        # Coupling strength   # -1.0 it first attemps
    J2 = -1.0,       # All-to-all coupling strength
    h = 5,          # Tree height
    p = 1,         # Small-world connection probability
    sigma = 1.0,     # Disorder strength
    max_time=1000,    # Maximum time for the simulation
    dt=0.1,           # Time step for the simulation
) -> Figure:
    
    ## Compute glued-trees state:
    gt = GluedTreesSmallWorld(h, J, J2, p, False, sigma, distribution="gaussian")
    res = full_analysis(gt, max_t=max_time, dt=dt)
    data = full_movie_figure_frame_at_time(res, t="Final")

    fig = data["fig"]
    fig_name = f"final_frame_{data['movie_title_str']}".replace(":", "")
    save_figure(fig, fig_name, extensions=["png"])

    return fig




def _kwargs_gen(param_name:str|None, vector:list|np.ndarray) -> Generator[dict, None, None]:
    if param_name is None: 
        yield {}
    else:
        for value in vector:
            yield {param_name: value}

j_vals = None

def capture_frames(
    param_name:str|None = 'J',
    vector:list|np.ndarray = j_vals,
):

    for kwargs in _kwargs_gen(param_name, vector):
        fig : Figure = _capture_frame(**kwargs)
        plt.close(fig)  # Close the figure to free memory

    pass


def _compute_center_frequency(freq_vect:np.ndarray, freq_response:np.ndarray):
    # Compute the magnitude squared of the frequency response
    magnitude_squared = np.abs(freq_response) ** 2
    # Compute the center frequency using the weighted average formula
    center_frequency = np.sum(freq_vect * magnitude_squared) / np.sum(magnitude_squared)
    
    return center_frequency


def _compute_average_value(
    time_vector: np.ndarray,
    exit_probabilities: np.ndarray, 
    method:Literal["simple", "trapezoidal"] = "simple"
) -> float:
    """
    Compute the average exit probability over the given time vector.
    """
    match method:
        case "simple":
            # Simple average good enough when the time vector is evenly spaced:
            sum_ = sum(exit_probabilities)
            average = sum_ / len(exit_probabilities)

        case "trapezoidal":
            # Alternatively, use trapezoidal integration for a more accurate average:
            average = np.trapezoid(exit_probabilities, time_vector) / (time_vector[-1] - time_vector[0])

        case _:
            raise ValueError(f"Unknown method: {method!r}. Use 'simple' or 'trapezoidal'.")
        
    return average


j_vals = np.linspace(-0.0001, -20, 51)
num_repats = 20  # Number of repetitions for each parameter value
max_time = 100


def _extract_results(
    *,
    J = -1.0,         # Coupling strength   # -1.0 it first attemps
    J2 = -1.0,        # All-to-all coupling strength
    h = 5,            # Tree height
    p = 1,            # Small-world connection probability
    sigma = 1.0,      # Disorder strength
    max_time=max_time,    # Maximum time for the simulation
    dt=0.05,           # Time step for the simulation
    rng:int = 0
):
    gt = GluedTreesSmallWorld(h, J, J2, p, False, sigma, distribution="gaussian", rng=rng)
    res = full_analysis(gt, max_t=max_time, dt=dt, prog_bar=False)
    freq_vect, freq_response = res.exit_probability_fourier_transform()
    center_frequency = _compute_center_frequency(freq_vect, freq_response)
    average_exit_probability = _compute_average_value(res.times, res.exit_probabilities)
    return center_frequency, average_exit_probability


def _add_item_to_dict_of_lists(d:dict[float, list[float]], key:float, value:float) -> None:
    if key in d:
        d[key].append(value)  
    else:
        d[key] = [value]

def plot_mean_frequency(
    param_name:str|None = 'J',
    vector:list|np.ndarray = j_vals,
    num_repats:int = num_repats

):

    freq_x_y_values_dict : dict[float, list[float]] = {}
    prob_x_y_values_dict : dict[float, list[float]] = {}

    prog_bar = ProgressBar(num_repats*len(vector), print_length=80)
    for kwargs in _kwargs_gen(param_name, vector):
        for i in range(num_repats):
            

            param_val = kwargs[param_name]
            kwargs['rng'] = i
            prog_bar.next(extra_str=f"Computing center frequency for {kwargs}")
            
            cent_freq, aver_prob = _extract_results(**kwargs)

            _add_item_to_dict_of_lists(freq_x_y_values_dict, param_val, cent_freq)
            _add_item_to_dict_of_lists(prob_x_y_values_dict, param_val, aver_prob)


    fig, freq_ax = new_figure()
    prob_ax = twin_axis(freq_ax)

    plot_with_spread(x_y_values_dict=freq_x_y_values_dict, axes=freq_ax, color="tab:blue")
    plot_with_spread(x_y_values_dict=prob_x_y_values_dict, axes=prob_ax, color="tab:red" )

    freq_ax.set_xlabel(param_name)
    freq_ax.set_ylabel('Center Frequency [Hz]')
    prob_ax.set_ylabel('Mean Exit Probability')
    prob_ax.set_title("Glued Trees Small World\nMean Center Frequency and Exit Probability")
    
    save_figure(file_name="mean_frequency_plot", extensions=["png", "svg", "pdf"])
    prog_bar.clear()
    pass


def main():
    # capture_movie()
    capture_frames()
    # plot_mean_frequency()

#%%



#%%

if __name__ == "__main__":
    main()
