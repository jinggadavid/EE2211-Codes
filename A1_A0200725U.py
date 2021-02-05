import numpy as np
from numpy.linalg import inv

# Please replace "MatricNumber" with your actual matric number here and in the filename
def A1_A0200725U(X, y):
    """
    Input type
    :X type: numpy.ndarray
    :y type: numpy.ndarray

    Return type
    :w type: numpy.ndarray
    :XT type: numpy.ndarray
    :InvXTX type: numpy.ndarray
   
    """
    # your code goes here
    XT = X.T
    InvXTX = inv(XT @ X)
    w = InvXTX @ X.T @ y

    # return in this order
    return w, XT, InvXTX
