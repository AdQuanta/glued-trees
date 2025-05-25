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

    parameters: dict[str, Any]

    times: NDArray[np.float64]
    states: list[Qobj]

    layer_distribution_at_time_steps : list[NDArray[np.float64]]
    exit_probabilities : list[float]
    

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

def simulate_time_evolution(gt:GluedTrees, max_t:float, dt:float) -> TimeEvolutionResultsType:
    return gt.time_evolution(max_t+dt, dt)


def compute_layer_distribution(gt:GluedTrees, res:TimeEvolutionResultsType) -> list[NDArray[np.float64]]:
    """
    Compute the layer distribution for each state in the time evolution results.
    """
    layer_distribution = []
    for state in res.states:
        layer_distribution.append(gt.get_layer_distribution(state))
    return layer_distribution


def full_analysis(gt:GluedTrees,
    max_t:float, dt:float
) -> FullAnalysisResults:
    """
    Get all statistics and results of the Glued Trees object.
    """
    ## Call analysis functions:
    time_evolution_results = simulate_time_evolution(gt=gt, max_t=max_t, dt=dt)

    ## Unpack results:
    parameters = gt.parameters
    times = np.array(time_evolution_results.times)
    states = time_evolution_results.states

    ## Layer distribution:
    layer_distributions_at_time_steps : list[NDArray[np.float64]] = compute_layer_distribution(gt, time_evolution_results)
    exit_probabilities = [layer[-1] for layer in layer_distributions_at_time_steps]
    
    return FullAnalysisResults(
        glued_trees=gt,
        time_evolution_results=time_evolution_results,
        parameters=parameters,
        times=times,
        states=states,
        layer_distribution_at_time_steps=layer_distributions_at_time_steps,
        exit_probabilities=exit_probabilities,
    )