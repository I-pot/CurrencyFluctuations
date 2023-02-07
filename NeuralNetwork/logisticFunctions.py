import numpy as np

def sigmoid(x):
    """The simple sigmoid function through the logistic function
    
    :param x: Preferably real number
    :returns: 1.0/(1.0 + np.exp(-x))
    """
    return 1.0/(1.0 + np.exp(-x))

def sigmoid_derivative(x):
    """The derivative of the sigmoid function through the logistic function
    
    :param x: Preferably real number
    :returns: np.exp(-x)/(1.0 + np.exp(-x))^2
    """
    #return x*(1 - x)
    return sigmoid(x)*(1.0 - sigmoid(x))

def sigmoidE(x,x0,L,k):
    """Extension of the simple sigmoid function through the logistic function
    
    :param x: Preferably real number
    :param x0: Sigmoid's midpoint
    :param L: Curve's maximum value
    :param k: Steepness of the curve
    :returns: 1.0/(1.0 + np.exp(-x))
    """
    return L/(1.0 + np.exp(-k(x-x0)))   

def tanh_derivative(x):
    """The derivative of tanh.
    
    :param x: Preferably real number
    :returns: 1/(np.cosh(x)*np.cosh(x))
    """
    return 1/(np.cosh(x)*np.cosh(x))
