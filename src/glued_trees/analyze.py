from typing import TypedDict, Any, Callable, TypeAlias
from numpy.typing import NDArray

from dataclasses import dataclass

from .classes import GluedTrees

from qutip import Qobj
from qutip import Result as TimeEvolutionResultsType
import numpy as np  



# =============================================================== #
#                         Helper Classes                          #
# =============================================================== #

@dataclass
class FullAnalysisResults: 

    """
    Class to store the results of the Glued Trees object.
    """
    glued_trees: GluedTrees
    time_evolution_results: TimeEvolutionResultsType
    sample_interval : float

    parameters: dict[str, Any]

    times: NDArray[np.float64]
    states: list[Qobj]

    layer_distribution_at_time_steps : list[NDArray[np.float64]]
    exit_probabilities : np.ndarray
    

    def layer_distribution_at_time(self, time:float) -> np.ndarray:
        """
        Get the layer distribution at a given time.
        """
        # Find the index of the time closest to the given time
        idx, _ = _find_value_closest_to_items_in_array(self.times, time)
        # Get the state at that time
        state = self.states[idx]
        # Use the GluedTrees object to get the layer distribution by state
        return self.glued_trees.get_layer_distribution(state)
    
    def _exit_probability_between_times(self, time_start:float=0.0, time_end:float|None=None) -> np.ndarray:
        """
        Calculate the exit probabilities signal, from start to end time.
        If end is None, it will use the last time in the times array.
        """
        ## Find the index of the time closest to the given times
        idx_start, time_start = _find_value_closest_to_items_in_array(self.times, time_start)
        if time_end is None:
            idx_end, time_end = len(self.times) - 1, self.times[-1]
        else:
            idx_end, time_end = _find_value_closest_to_items_in_array(self.times, time_end)

        ## exit probabilities in the range:
        exit_probabilities_at_times = self.exit_probabilities[idx_start : idx_end+1]


        return exit_probabilities_at_times
    
    def exit_probability_fourier_transform(self, time_start:float=0.0, time_end:float|None=None) -> tuple[np.ndarray, np.ndarray]:
        """
        Calculate the Fourier transform of the exit probabilities signal, from start to end time.
        If end is None, it will use the last time in the times array.
        """

        exit_probabilities_at_times = self._exit_probability_between_times(time_start, time_end)
        dt = self.sample_interval

        ## Fourier transform:
        freq_response = np.fft.rfft(exit_probabilities_at_times)
        freq_vect = np.fft.rfftfreq(len(exit_probabilities_at_times), d=dt)

        return freq_vect, freq_response





# =============================================================== #
#                       Helper Functions                          #
# =============================================================== #
def _find_value_closest_to_items_in_array(array:np.ndarray, value:float) -> tuple[int, float]:
    """
    Find the index of the value in the array that is closest to the given value.
    Return both the index and the closest value in the array.
    """
    idx = np.argmin(np.abs(array - value))
    correct_val = array[idx]
    return int(idx), correct_val

# =============================================================== #
#                       Global Functions                          #
# =============================================================== #

def simulate_time_evolution(gt:GluedTrees, max_t:float, dt:float, prog_bar:bool=True) -> TimeEvolutionResultsType:
    return gt.time_evolution(max_t+dt, dt, prog_bar=prog_bar)


def compute_layer_distribution(gt:GluedTrees, res:TimeEvolutionResultsType) -> list[NDArray[np.float64]]:
    """
    Compute the layer distribution for each state in the time evolution results.
    """
    layer_distribution = []
    for state in res.states:
        layer_distribution.append(gt.get_layer_distribution(state))
    return layer_distribution


def full_analysis(
    gt:GluedTrees,
    max_t:float, 
    dt:float,
    prog_bar:bool=True
) -> FullAnalysisResults:
    """
    Get all statistics and results of the Glued Trees object.
    """
    ## Call analysis functions:
    time_evolution_results = simulate_time_evolution(gt=gt, max_t=max_t, dt=dt, prog_bar=prog_bar)

    ## Unpack results:
    parameters = gt.parameters
    times = np.array(time_evolution_results.times)
    states = time_evolution_results.states

    ## Layer distribution:
    layer_distributions_at_time_steps : list[NDArray[np.float64]] = compute_layer_distribution(gt, time_evolution_results)
    exit_probabilities = np.array([layer[-1] for layer in layer_distributions_at_time_steps])
    
    return FullAnalysisResults(
        glued_trees=gt,
        time_evolution_results=time_evolution_results,
        parameters=parameters,
        times=times,
        sample_interval=dt,
        states=states,
        layer_distribution_at_time_steps=layer_distributions_at_time_steps,
        exit_probabilities=exit_probabilities,
    )