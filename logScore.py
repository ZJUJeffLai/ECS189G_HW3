import math
FILE = 'exampleResult'
output = [i for i in open(FILE,'r')]
result = 0
for i in output:
    result -= math.log(float(i.split()[1]),2)
result = result / len(output)
result = math.pow(2, result)
print result
