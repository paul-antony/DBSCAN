#
#
# Task Name:        Implementation of DBSCAN algorithm without using numpy
# Author List:      Job Jacob, Paul Antony
# File Name:        dbscan.py
# Functions:        dataRead(), DBSCAN.__init__(), DBSCAN.displayDataset(), DBSCAN.runDBSCAN(), DBSCAN.growCluster(), DBSCAN.regionQuery(),
#                   DBSCAN.EuclideanDistance(), DBSCAN.createClusterList(), DBSCAN.createNoiseList(), DBSCAN.displayClusters(), DBSCAN.displayNoise()
# Global variables: None
#
#
import csv

# The DBSCAN class contains all the functions required to run the DBSCAN clustering on the input dataset
class DBSCAN:
	#
	#
	# Function Name:    __init__()
	# Input:            1) self --> the object of the class
	#                   2) D --> the dataset
	#                   3) eps --> the maximum distance between two data vectors for them to be neighbors
	#                   4) MinPts --> the minimum neighbors a vector should have in order for it to be a part of the same cluster
	# Output:           None
	# Logic:            This function is used to initialize the DBSCAN object variables.
	# Example Call:     DBSCAN.__init__(D, 5, 2)
	#
	#
	def __init__(self, D, eps, MinPts):
		self.D = D
		self.labels = [0]*len(D)
		self.C = 0
		self.eps = eps
		self.MinPts = MinPts

	#
	#
	# Function Name:    displayDataset()
	# Input:            self --> the object of the class
	# Output:           None
	# Logic:            This function is used to display the dataset read from the csv file (stored in a list D).   
	# Example Call:     self.displayDataset()
	#
	#
	def displayDataset(self):
		for i in range(0, len(self.D)):
			print (i+1, "	", self.D[i])
		print("")
		
	#	
	#
	# Function Name:    runDBSCAN()
	# Input:            self --> the object of the class
	# Output:           None
	# Logic:            This function is used to start a new cluster and call the growCluster() function to grow that particular cluster. First we check if a 
	#                   vector in the dataset D is assigned a cluster or noise value (list labels is used to assign this value | -1 for noise and the cluster 
	#                   number for a cluster). If yes (i.e, D's corresponding labels index value is either -1 or a cluster number), then we move to the next 
	#                   vector. If no (i.e, D's corresponding labels index value is 0), then it means that the vector has not been evaluated. Then we check if 
	#                   that particular vector has any neighbors. If the vector has the specified minimum neighbors, then the vector is assigned as a new cluster
	#                   and the growCluster() function is invoked to expand the cluster even further. If the vector has less than the specified neighbors,
	#                   then the vector is declared as a noise and we move to the next vector in the list.	
	# Example Call:     self.runDBSCAN()
	#
	#
	def runDBSCAN(self):  
		for P in range(0, len(self.D)):
			if not (self.labels[P] == 0):
				continue
			NeighborPts = self.regionQuery(P)
			if len(NeighborPts) < self.MinPts:
				self.labels[P] = -1  
			else: 
				self.C += 1
				self.labels[P] = self.C
				self.growCluster(P)
    
	#
	#
	# Function Name:    growCluster()
	# Input:            1) self --> the object of the class
	#                   2) P --> the index of the vector starting the new cluster
	# Output:           None
	# Logic:            This function is used to further expand a cluster created by runDBSCAN() function. It takes the neighboring vectors of a cluster
	#                   vector and add it to a queue. These neighboring vectors are then evaluated to check if they are a part of the cluster. If yes, then
	#                   they are added to the cluster by changing their corresponding labels index value to the cluster number. This process continues as 
	#                   long as all the neighboring points of the cluster vectors are evaluated.
	# Example Call:     self.growCluster(P)
	#
	#
	def growCluster(self, P):
		SearchQueue = [P]
		i = 0
		while i < len(SearchQueue):        
			P = SearchQueue[i]
			NeighborPts = self.regionQuery(P) 
			if len(NeighborPts) < self.MinPts:
				i += 1
				continue
			for Pn in NeighborPts:
				if self.labels[Pn] == -1:
					self.labels[Pn] = self.C   
				elif self.labels[Pn] == 0:
					self.labels[Pn] = self.C
					SearchQueue.append(Pn)
			i += 1        
    
	#
	#
	# Function Name:    regionQuery()
	# Input:            1) self --> the object of the class
	#                   2) P --> the index of the vector that requires evaluation
	# Output:           neighbors --> the list of neighbors of the given vector
	# Logic:            This function is used to find the neighboring points (vectors) of a given vector.   
	# Example Call:     self.regionQuery(P)
	#
	#
	def regionQuery(self, P):
		neighbors = []
		for Pn in range(0, len(self.D)):
			if self.EuclideanDistance(self.D[P], self.D[Pn]) < self.eps:
				neighbors.append(Pn) 
		return neighbors

	#
	#
	# Function Name:    EuclideanDistance()
	# Input:            1) self --> the object of the class
	#                   2) pt1 --> the first vector
	#                   3) pt2 --> the second vector
	# Output:           distance --> the distance between the two vectors
	# Logic:            This function is used to find the distance between two vectors.   
	# Example Call:     self.EuclideanDistance(self.D[P], self.D[Pn])
	#
	#
	def EuclideanDistance(self, pt1, pt2):
		sum = 0
		distance = 0
		for i in range(len(pt1)):
			sum += (pt1[i] - pt2[i])**2
		distance = sum**(1/2)
		return distance
    
	#
	#
	# Function Name:    createClusterList()
	# Input:            self --> the object of the class
	# Output:           ClusterList --> a 2D list with the different clusters and their corresponding vector elements 
	# Logic:            This function is used to create a 2D list with the different clusters and their corresponding vector elements.
	# Example Call:     self.createClusterList()
	#
	#
	def createClusterList(self):
		ClusterList = []
		for i in range(0, self.C):
			cluster = []
			for j in range(0, len(self.labels)):
				if self.labels[j] == i+1:
					cluster.append(self.D[j])
			ClusterList.append(cluster)
		return ClusterList

	#
	#
	# Function Name:    createNoiseList()
	# Input:            self --> the object of the class
	# Output:           NoiseList --> a list containing all the noise vectors obtained after the clustering 
	# Logic:            This function is used to create a list containing all the noise vectors obtained after the clustering.
	# Example Call:     self.createNoiseList()
	#
	#
	def createNoiseList(self):
		NoiseList = []
		for i in range(0, len(self.labels)):
			if self.labels[i] == -1:
				NoiseList.append(self.D[i])
		return NoiseList

	#
	#
	# Function Name:    displayClusters()
	# Input:            self --> the object of the class
	# Output:           None
	# Logic:            This function is used to display all the clusters and their vector elements.
	# Example Call:     self.displayClusters()
	#
	#
	def displayClusters(self):
		ClusterList = self.createClusterList()
		for cluster in ClusterList:
			print("Cluster", ClusterList.index(cluster)+1,)
			for item in cluster:
				print(item)
			print("")

	#
	#
	# Function Name:    displayNoise()
	# Input:            self --> the object of the class
	# Output:           None
	# Logic:            This function is used to display all the noise vectors.
	# Example Call:     self.displayNoise()
	#
	#
	def displayNoise(self):
		NoiseList = self.createNoiseList()
		for noise in NoiseList:
			print(noise)
		print("")	

#
#
# Function Name:    dataRead()
# Input:            FileName --> the name or location of the csv file to read the dataset from
# Output:           D --> the dataset read from the csv file 
# Logic:            This function is used to read the dataset from the input csv file and store it in the output list D.
# Example Call:     dataRead('DBSCAN_data.csv')
#
#		
def dataRead(FileName):
	D = []
	with open(FileName, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			A = []
			for data in row:
				A.append(float(data))
			D.append(A)
	return D


