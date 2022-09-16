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

        self.data = data
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

    def plot_histogram(self):
        """The method to plot the hisogram of the data

        Args:
            None

        Returns: 
              None
        
        """
        plt.hist(self.data)
        plt.title("Distribution of data")
        plt.xlabel("data")
        plt.ylabel("Frequency")

    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)
        

    def plot_histogram_pdf(self, n_spaces = 50):

        """Function to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)
        
         # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y