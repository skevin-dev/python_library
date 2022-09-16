import math
from statistics import stdev 
import matplotlib.pyplot as plt 
import numpy as np

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

    def calculate_mean(self):
        """The method to calculate the mean of the data set

        Args:

             None 

        Returns:

            float: the mean of the dataset 
        
        """

        mean_dataset =  np.mean(self.data)
        self.mean = mean_dataset

        return self.mean


    def calculate_stdev(self,sample=True):
        """The method to calculate the standard deviation of the data set

        Args:
           
            sample(bool) whether the data represent a sample or population

        Returns:
             
             float: the standard deviation of the dataset 
        
        """

        if sample:
            n = len(self.data) -1 

        else:
            n = len(self.data)

        variance = sum((x-self.mean)**2 for x in self.data)

        stdev_dataset = math.sqrt(variance/n)

        self.stdev = stdev_dataset

        return self.stdev

    def read_data_file(self,filepath,sample=True):
        """The method to read in data from txt file. the text file should have one number
        per line. After reading in the file, the mean and standard deviation are calculated 

        Args:

            file_name(file): file containing data 

        returns: 
               
               None 
        
        
        """

        with open(filepath) as file:
            data = []
            line = file.readline()
            while line:
                data.append(int(line))
                line = file.readline()
        file.close()

        self_data = data
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

