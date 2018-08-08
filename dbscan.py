import csv

class DBSCAN:
	def __init__(self, D, eps, MinPts):
		self.D = D
		self.labels = [0]*len(D)
		self.C = 0
		self.eps = eps
		self.MinPts = MinPts

    #displays data set
	def displayDataset(self):
		for i in range(0, len(self.D)):
			print (i+1, "	", self.D[i])
		print("")
    #starts DBSCAN clustering
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
    #grows a cluster
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
    
    #finds neighbor points
	def regionQuery(self, P):
		neighbors = []
		for Pn in range(0, len(self.D)):
			if self.EuclideanDistance(self.D[P], self.D[Pn]) < self.eps:
				neighbors.append(Pn) 
		return neighbors
    #distance between two points
	def EuclideanDistance(self, pt1, pt2):
		sum = 0
		distance = 0
		for i in range(len(pt1)):
			sum += (pt1[i] - pt2[i])**2
		distance = sum**(1/2)
		return distance
    
    #creats list of cluster points
	def createClusterList(self):
		ClusterList = []
		for i in range(0, self.C):
			cluster = []
			for j in range(0, len(self.labels)):
				if self.labels[j] == i+1:
					cluster.append(self.D[j])
			ClusterList.append(cluster)
		return ClusterList

    #creats list of noice points
	def createNoiseList(self):
		NoiseList = []
		for i in range(0, len(self.labels)):
			if self.labels[i] == -1:
				NoiseList.append(self.D[i])
		return NoiseList

	def displayClusters(self):
		ClusterList = self.createClusterList()
		for cluster in ClusterList:
			print("Cluster", ClusterList.index(cluster)+1,)
			for item in cluster:
				print(item)
			print("")

	def displayNoise(self):
		NoiseList = self.createNoiseList()
		for noise in NoiseList:
			print(noise)
		print("")	

#used to read csv file and create list of points		
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


