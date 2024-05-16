def test_optimize():
    import numpy  # engine for numerical computing
    from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
    from pypop7.optimizers.rs.bes import BES
    problem = {'fitness_function': rosenbrock,  # define problem arguments
               'ndim_problem': 2,
               'lower_boundary': -5.0 * numpy.ones((2,)),
               'upper_boundary': 5.0 * numpy.ones((2,))}
    options = {'max_function_evaluations': 5000,  # set optimizer options
               'seed_rng': 2022,
               'x': 3 * numpy.ones((2,)),
               'n_individuals': 10,
               'c': 0.1,
               'lr': 0.000001}
    bes = BES(problem, options)  # initialize the optimizer class
    results = bes.optimize()  # run the optimization process
    assert results['n_function_evaluations'] == 5000
    assert results['best_so_far_y'] < 1.0
