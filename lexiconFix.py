pann = [i for i in open('jenLexicon','r')]
brown = [i for i in open('jenBrown','r')]
tagSet = set()
missingLex = []
enter = 0
for line in pann:
    if not len(line[:-1].split()) in[0,1,2]:
        tagSet.add(line.split()[0])

for line in pann:
    if len(line[:-1].split()) in[1,2]:
        for brownline in brown:
            word = brownline.split()
            if '->' in word and word[2]== line[:-1]:
                enter = 1
                if not word[0] in tagSet:
                    print '==============================>', 
                print brownline[:-1]
        if enter == 0:
            missingLex.append(line[:-1])
        enter = 0

for i in missingLex:
    print i