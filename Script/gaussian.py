import math 
import matplotlib.pyplot as plt 

class Gaussian():
    """ Gaussian distribution class for calculating and 
    visualizing a gaussian distribution

    Attributes:
        mean(float) representing the mean value of the distribution
        stdev(float) representing the standard deviation of the distribution
        data_list(list of floats) a list of floats extracted from the data file
    """

    def __init__(self,mu=0,sigma=1):
        self.mean = mu
        self.stdev = sigma
        self.data = []

        