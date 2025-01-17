# Author: Olivia Guest (oliviaguest)
# Original publication of this code available at https://github.com/oliviaguest/gini/blob/master/gini.py

import numpy as np


def gini(array):
    """Calculate the Gini coefficient of a numpy array.
    """
    # based on bottom eq:
    # http://www.statsdirect.com/help/generatedimages/equations/equation154.svg
    # from:
    # http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    # All values are treated equally, arrays must be 1d and dtype=float
    array = array.flatten()
    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    # Values cannot be 0:
    array += 0.0000001
    # Values must be sorted:
    array = np.sort(array)
    # Index per array element:
    index = np.arange(1, array.shape[0]+1)
    # Number of array elements:
    n = array.shape[0]
    # Gini coefficient:
    return (np.sum((2 * index - n - 1) * array)) / (n * np.sum(array))


# if __name__ == '__main__':
#     a = np.array([5, 6, 7, 0, -93, 1], dtype='float64')
#     print(f'The gini coefficient is: {gini(a):0.5f}')
