# Sagatovot īsu skaidrojumu NumPy funkcijām, kas izmantotas nodarbības Python programmas piemērā

from numpy import *
import operator

# funkcija, kas atgriež iepriekš nodefinētu divdimensiju masīvu un masīvu ar nosaukumiem
def createDataSet():
	group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels

# klasificē datus
def classify0 (inX, dataSet, labels, k):
	# nodefinē datu masīva apjomu
	dataSetSize = dataSet.shape[0]
	# paplašina masīvu inX reizes tik, cik masīva apjoms dataSetSize
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	classCount = { }
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(),
	    key = operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

# ============
Grupas, Kategorijas = createDataSet()
print ("Kategorijas: ", Kategorijas)
print ("Grupas: \n", Grupas)
# Klasificē punktus pa grupām
print("Punkts ar pazimem  1 un 1 atrodas ",
classify0([1,1], Grupas, Kategorijas, 3),
" grupā.")
