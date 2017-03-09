
#def storeVectors(vectorCount, caseNumber):
#	count = vectorCount
#	for caseCount in xrange(2, caseNumber+2):
#		n =


def sort(list):
	l = list
	l.sort()
	return l

def reverseSort(list):
	l = list
	l.sort(reverse = True)
	return l

def minimumProduct(v1, v2):
	v1 = sort(v1)
	v2 = reverseSort(v2)
	return [v1 * v2 for v1,v2 in zip(v1, v2)]

if __name__ == "__main__" :
	case = int(raw_input())
	for caseCount in xrange(1, case+1):
		i = 0
		vecSet = []
		addToVec = vecSet.append 
		while i < 3:
			n = [int(s) for s in raw_input().split(" ")]
			addToVec(n)
			i += 1
		print ("Case #%i: %s" % (caseCount, vecSet))
