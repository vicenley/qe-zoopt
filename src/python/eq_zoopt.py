import zoopt
from zquantum.core.interfaces.optimizer import Optimizer  
from scipy.optimize import OptimizeResult 
import numpy as np
import copy

class ZOOPTOptimizer(Optimizer):
    def __init__(self, iterations):
        self.iterations = options


    def minimize(self, cost_function, initial_params):
        '''minimize using the zeroth order optimization algorithm
           Args:
            cost function: the function to minized.
            initial_params: starting point for the optimization process. 
           Returns:
            tuple: optimization results dict and the optimized parameters.
        '''
        def zoopt_help_function(self, solution):
            params = solution.get_x()
            value = cost_function(params)
            history.append({'params': params, 'value': value})
            print(f'Function evaluation {len(history)}: {value}', flush=True)
            print(f'{params}', flush=True)
            return value 
        
        dim_size = np.shape(initial_params)
        range_dim = [[]]*dim_size
        min_bounds = [-np.pi for _ in range(dim_size)]
        max_bounds = [np.pi for _ in range(dim_size)]
        for i in range(dim_size):
            range_dim[i] = [min_bounds[i],max_bounds[i]]

        dim = zoopt.Dimension(dim_size, range_dim, [True]*dim_size)
        objective = zoopt.Objective(zoopt_help_function,dim)
        par = zoopt.Parameter(budget = self.iterations)

        result = zoopt.Opt.min(objective, par)

        optimization_results = {}
        optimization_results['opt_value'] = result.get_value()
        optimization_results['opt_params'] = result.get_x()
        optimization_results['history'] = history

    return OptimizeResult(opt_results)
