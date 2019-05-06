import sys
import statistics

dataType = sys.argv[1]
fileName = str(sys.argv[2])
iterations = int(sys.argv[3])

resultFile = [l[:-1] for l in open(fileName, 'rt').readlines()]
fileList = []
for line in resultFile:
    fileList.append(line)

x = fileName.index("Result")
outputName = fileName[0:x] + str(dataType) +"Calculations.txt"
outputFile = open(outputName, 'w')

percentList = []
for line in fileList:
    if '%' in line:
        start = line.index('(') + 2
        end = line.index('%') - 1
        temp = str(line[start:end])
        real_num = str(temp[0]) + str(temp[2]) + str(temp[4]) + str(temp[6])
        real_num = float(real_num)
        percentList.append(real_num)


outputFile.write(dataType)
outputFile.write('\n')
for i in ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%']:
    smallList = []
    for j in range(iterations):
        smallList.append(percentList.pop(0))
    
    average = statistics.mean(smallList)
    std_dev = statistics.stdev(smallList)
    message = i + ": " + str(smallList) + "  " + "Accuracy: " + str(average) + "  Standard Deviation: " + str(std_dev) + '\n'
    outputFile.write(message)