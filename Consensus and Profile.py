def readFile(filePath):
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

FASTAFile = readFile('rosalind_cons.txt')
FASTADict = {}
FASTALabel = ''

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ''
    else:
        FASTADict[FASTALabel] += line

table = [value for key, value in FASTADict.items()]
print(table)

def dna_consensus(table, n):
    dic = {}
    for x in table:
        if x[n] in 'ACGT':
            if x[n] in dic:
                dic[x[n]] += 1
            else:
                dic[x[n]] = 1
        else:
            continue
    return dic

t = []
for n in range(0, len(table[0])):
    t.append(dna_consensus(table, n))
    for x in 'ACGT':
        if t[n].get(x) == None:
            t[n][x] = 0
    print(max(t[n], key = t[n].get), end='')
print(t)

