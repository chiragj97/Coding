def weightedMean(x,w):
    sumNumerator = 0
    sumDenominator = 0
    for i in range(len(x)):
        sumNumerator += x[i]*w[i]
    for j in range(len(x)):
        sumDenominator += w[j]
    weightedMean = sumNumerator/sumDenominator
    return weightedMean

n = int(input())
x = list(map(int, input().strip().split()))[:n]
w = list(map(int, input().strip().split()))[:n]
weightedMean = weightedMean(x,w)
print("Weighted Mean is : " +weightedMean)


