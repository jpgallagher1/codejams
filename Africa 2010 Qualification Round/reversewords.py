fname = "B-large-practice.in.txt"


def importData(filePath):
    textArray = open(filePath)
    listOfArgs = []
    appendToListOfArgs = listOfArgs.append
    for line in textArray:
        line = line.strip('\n')
        yield line
def reversal(string):
    return ' '.join(string.split()[::-1])

def caseReporter(listOfReversedStrings):
    i = 0
    while i < len(listOfReversedStrings):
        print("case #" + str(i+1) + ": " + listOfReversedStrings[i])
        i+=1

caseReporter([reversal(x) for x in importData(fname)][1:])