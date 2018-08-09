#
#
# Task Name:        Implementation of DBSCAN algorithm without using numpy
# Author List:      Job Jacob, Paul Antony
# File Name:        graphplot.py
# Functions:        plot()
# Global variables: None
#
#
import matplotlib.pyplot as plt

#
#
# Function Name:    plot()
# Input:            1) ClusterList --> a 2D list with the different clusters and their corresponding vector elements 
#                   2) NoiseList --> a list containing all the noise vectors obtained after the clustering 
# Output:           None
# Logic:            This function is used to plot a graph for the different clusters and noise vectors.
# Example Call:     plot(ClusterList, NoiseList)
#
#
def plot(ClusterList, NoiseList):
	i = 0
	color = ['b', 'g', 'r', 'c', 'm', 'y']
	for cluster in ClusterList:
		x = []
		y = []
		for item in cluster:
			x.append(item[0])
			y.append(item[1])
		plt.plot(x, y, color[i]+".")
		i += 1
	x = []
	y = []
	for noise in NoiseList:
		x.append(noise[0])
		y.append(noise[1])
	plt.plot(x, y, color[i]+".")
	plt.axis([0, 200, 0, 200])
	plt.show()
	


