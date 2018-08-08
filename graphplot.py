import matplotlib.pyplot as plt

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
	


