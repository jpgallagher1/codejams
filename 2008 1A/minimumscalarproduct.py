fname = "A-small-practice.in.txt"

def importData(filePath):
	for line in open(filePath):
		yield map(int, (line.strip()).split())

def calculate(listOfVectors):
	caseCount = listOfVectors[0]
	vectorCount = 0
	vectors = []
	i = 0
	while i < caseCount[0]:
		vectorDescriptorCheck = listOfVectors[i+1]
		if len(vectorDescriptorCheck) == 1:
			vectorCount = vectorDescriptorCheck
			v1 = listOfVectors[i+2]
			v2 = listOfVectors[i+3]
			v1.sort()
			v2.sort()
			v2.reverse()
			print [v1*v2 for v1,v2 in zip(v1,v2)]
		else:
			pass
		i += 3
	return vectors





calculate([x for x in importData(fname)])