
def ccomplexity_rater(other_function):
    '''
    This function calculates the radian complexity of other functions.
    Radian complexity is used as a proxy for cognitive complexity. Ie how hard is a code block to understand.

    Inputs: Other Python functions.
    Side Effects: print's informative strings about complexity.
    Outputs: A scalar value that is located within the interval 1-41. The scalar is used with
    A printed guide.
    !pip install radon inspect

    Use python introspection to convert other_function to a string representation of the
    source code, the function was made from.

    '''
    import inspect, radon, pprint
    from radon.complexity import cc_rank, cc_visit
    f_source_code = "".join(inspect.getsourcelines(other_function)[0])
    results = radon.complexity.cc_visit(f_source_code)
    ranking = radon.complexity.sorted_results(results)
    pp = pprint.PrettyPrinter(indent=4)
    ranking_guide = ''' From:   http://radon.readthedocs.io/en/latest/api.html \n
    1 - 5 A (low risk - simple block) \n
    6 - 10 B (low risk - well structured and stable block) \n
    11 - 20 C (moderate risk - slightly complex block) \n
    21 - 30 D (more than moderate risk - more complex block) \n
    31 - 40 E (high risk - complex block, alarming) \n
    41+ F (very high risk - error-prone, unstable block) \n
    '''
    pp(ranking_guide)
    actual_value = ranking[0][-1]
    pp('cognitive complexity is: {}'.format(actual_value))
    if actual_value > 10:
        pp('Consider rewriting your code it might be hard for you and others to understand, and therefore maintain')
    else:
        pp('Good work keep writing modular, readable, and simple code')

    return ranking[0][-1]
from neuronunit.optimization.nsga_parallel import nunit_evaluation
results, ranking = ccomplexity_rater(nunit_evaluation)
print(ranking)
