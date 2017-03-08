fname = "A-small-practice.in.txt"

def importData(filePath):
	caseCount = 0
	for line in open(filePath):
		print map(int, (line.strip()).split())

importData(fname)