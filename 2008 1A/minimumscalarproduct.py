
#def calculate(listOfVectors):
#	caseCount = listOfVectors[0]
#	vectorCount = 0
#	vectors = []
#	i = 0
#	while i < caseCount[0]:
#		vectorDescriptorCheck = listOfVectors[i+1]
#		if len(vectorDescriptorCheck) == 1:
#			vectorCount = vectorDescriptorCheck
#			v1 = listOfVectors[i+2]
#			v2 = listOfVectors[i+3]
#			v1.sort()
#			v2.sort()
#			v2.reverse()
#			print [v1*v2 for v1,v2 in zip(v1,v2)]
#		else:
#			pass
#		i += 3
#	return vectors

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
		n = [int(s) for s in raw_input().split(" ")]
		
		print ("Case #%i: %s" % (caseCount, sort(n)))
