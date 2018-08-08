import dbscan
import graphplot

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


