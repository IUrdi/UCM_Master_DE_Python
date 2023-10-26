import numpy as np


def read_data(fname: str, tipo: type) -> np.ndarray:
    """
    function that reads a text file named fname and returns a ndarray with the values found in it
    :param fname: str
    :param tipo: type
    :return: ndarray
       a ndarray of tipo type values
    Examples:
    --------
    >>> read_data('./datos/zonas.txt',tipo=np.int_)
    array([[1, 1, 1, 1, 3, 3],
           [1, 1, 1, 1, 3, 1],
           [2, 2, 3, 3, 3, 4],
           [2, 2, 3, 3, 3, 4],
           [2, 2, 3, 3, 2, 2],
           [3, 3, 3, 3, 3, 2]])
    >>> read_data('./datos/valores.txt',tipo=np.float_)
    array([[5., 3., 4., 4., 4., 2.],
           [2., 1., 4., 2., 6., 3.],
           [8., 4., 3., 5., 3., 1.],
           [4., 2., 4., 3., 2., 2.],
           [6., 3., 3., 7., 4., 2.],
           [5., 5., 2., 3., 1., 3.]])
    >>> read_data('inexistentfile.txt',tipo=np.int_)
    Traceback (most recent call last):
        ...
    FileNotFoundError: Input file inexistentfile.txt not found
    """
    
    # Escribe aquí tu código
    # No olvides documentar la función
    try:
        return np.loadtxt(fname,dtype=tipo)
    except FileNotFoundError:
        raise FileNotFoundError(f'Input file {fname} not found')
        

def set_of_areas(zonas: np.ndarray)-> set[int]:
    """
    function that returns a set with unique/distinct values found in a ndarray of integers
    :param zonas: ndarray
    :return: set
       a set of integers
    Examples:
    --------
    >>> set_of_areas(np.arange(10).reshape(5, 2))
    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    >>> set_of_areas(np.zeros(10, dtype=np.int_).reshape(5, 2))
    {0}
    >>> set_of_areas(np.array([2, 3, 4, 2, 3, 4], dtype=np.int_).reshape(3, 2))
    {2, 3, 4}
    >>> set_of_areas(np.zeros(3, dtype=np.float_))
    Traceback (most recent call last):
        ...
    TypeError: The elements type must be int, not float64
    """
    # Escribe aquí tu código
    # No olvides documentar la función
    if zonas.dtype!='int':
        raise TypeError("The elements type must be int, not {}".format(zonas.dtype))
    return set(zonas.flatten())


def mean_areas(zonas: np.ndarray,valores: np.ndarray)-> np.ndarray:
    """
    function that returns the mean values of the different areas
    :param zonas: ndarray
    :param valores: ndarray
    :return: set
       a set of integers
    Examples:
    --------
    >>> mean_areas(np.array([[1, 1, 1, 1, 3, 3],[1, 1, 1, 1, 3, 1]]),np.array([[5., 3., 4., 4., 4., 2.],[2., 1., 4., 2., 6., 3.]]))
    array([[3.1, 3.1, 3.1, 3.1, 4. , 4. ],
           [3.1, 3.1, 3.1, 3.1, 4. , 3.1]])
    >>> mean_areas(np.array([[1.5, 1.9, 1, 1, 3, 3],[1, 1, 1, 1, 3, 1]]),np.array([[5., 3., 4., 4., 4., 2.],[2., 1., 4., 2., 6., 3.]]))
    Traceback (most recent call last):
        ...
    TypeError: The elements type must be int, not float64
    >>> mean_areas(np.array([[2,3], [4,5]]), np.array([[1,2,3], [4,5,6]]))  # dimensiones distintas
    Traceback (most recent call last):
        ...
    IndexError: Shape of zonas and valores must be the same. zonas: (2, 2) != valores: (2, 3)
    """
    # Check input array dimensions
    if zonas.dtype!='int':
        raise TypeError("The elements type must be int, not {}".format(zonas.dtype))
    if zonas.shape != valores.shape:
        raise IndexError(f'Shape of zonas and valores must be the same. zonas: {zonas.shape} != valores: {valores.shape}')
    conjunto=set(zonas.flatten())
    resMean=np.copy(valores)
    for zona in conjunto:
        mask = (zonas==zona)
        resMean[mask]=valores[mask].mean().round(1)
    return resMean




# ------------ test  --------#
import doctest

def test_doc()-> None:
    """
    The following instructions are to execute the tests of same functions
    If any test is fail, we will receive the notice when executing
    :return: None
    """
    doctest.run_docstring_examples(read_data, globals(), verbose=False)  # vemos los resultados de los test que fallan
    doctest.run_docstring_examples(set_of_areas, globals(), verbose=False)  # vemos los resultados de los test que fallan
    doctest.run_docstring_examples(mean_areas, globals(), verbose=False)  # vemos los resultados de los test que fallan


if __name__ == "__main__":
    test_doc()   # executing tests
