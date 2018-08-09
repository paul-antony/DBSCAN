#
#
# Task Name:        Implementation of DBSCAN algorithm without using numpy
# Author List:      Job Jacob, Paul Antony
# File Name:        main.py
# Functions:        main()
# Global variables: None
#
#
import dbscan
import graphplot

#
#
# Function Name:    main()
# Input:            None
# Output:           None
# Logic:            This function acts as a controller for the whole task. This includes declaring the FileName, eps & MinPts, and also calling the 
#                   required functions to complete the DBSCAN clustering and to plot its corresponding graph.
# Example Call:     main()
#
#
def main():
	FileName = 'DBSCAN_data.csv'
	eps = 5
	MinPts = 2
	print("\nImporting csv file", FileName, "...")
	D = dbscan.dataRead(FileName)
	print("IMPORTING COMPLETE\n")
	obj = dbscan.DBSCAN(D, eps, MinPts)
	print("The input dataset for our clustering is:")
	obj.displayDataset()
	print("Running DBSCAN clustering...")
	obj.runDBSCAN()
	print("CLUSTERING COMPLETE\n")
	print("The clusters are:")
	obj.displayClusters()
	print("The noise obtained after clustering are:")
	obj.displayNoise()
	ClusterList = obj.createClusterList()
	NoiseList = obj.createNoiseList()
	graphplot.plot(ClusterList, NoiseList)
	
main()


