'''
Problem

The Constitution of a certain country states that the leader is the
person with the name containing the greatest number of different
alphabet letters.
(The country uses the uppercase English alphabet from A through Z.)
For example, the name GOOGLE has four different alphabet letters:
E, G, L, and O.
The name APAC CODE JAM has eight different letters.
If the country only consists of these 2 persons,
APAC CODE JAM would be the leader.

If there is a tie, the person whose name comes earliest
in alphabetical order is the leader.

Given a list of names of the citizens of the country,
can you determine who the leader is?

Input

The first line of the input gives the number of test cases, T.
T test cases follow.
Each test case starts with a line with an interger N,
the number of people in the country.
Then N lines follow.
The i-th line represents the name of the i-th person.
Each name contains at most 20 characters
and contains at least one alphabet letter.

Output

For each test case, output one line containing
Case #x: y,
where x is the test case number (starting from 1)
and y is the name of the leader.

Small dataset

Each name consists of at most 20 characters and only consists of the
uppercase English letters A through Z.

Large dataset

Each name consists of at most 20 characters and only consists of the
uppercase English letters A through Z and ' '(space).
All names start and end with alphabet letters.
'''

fname = "A-small-practice.in.txt"


def importData(filePath):
    textArray = open(filePath)
    listOfArgs = []
    appendToListOfArgs = listOfArgs.append
    for line in textArray:
        line = line.strip('\n')
        appendToListOfArgs(line)
    for line in listOfArgs[1:]:
        if line[:1].isalpha() is not True:
            yield (listOfArgs[list(listOfArgs).index(line) + 1:
                list(listOfArgs).index(line) + int(line) + 1])
        else:
            pass
#
#
#def tie(charsList):
#
#    return np.sort(charsList, kind='mergesort')
#
## alphabetize first, then check for sets
#
#
#def standings(charsList):
#    li = map(len, map(list, (map(set, charsList))))
#    li.sort()
#    return li



print [x for x in importData(fname)][0]





