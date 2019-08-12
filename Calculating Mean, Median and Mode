def mean(n):
    sum = 0
    for i in range(len(n)):
        sum += n[i]
    mean = round((sum/len(n)), 1)
    return mean

def median(n):
	if((len(n) % 2) == 0):
		median = (n[int(len(n)/2)] + n[int((len(n)-1)/2)])/2
	else:
		median = round(n[int((len(n)/2))],1)
	return median 	

def sort(n):
	for i in range(len(n) - 1):
		for j in range(len(n) - 1):
			if(n[j] > n[j + 1]):
				temp = n[j]
				n[j] = n[j + 1]
				n[j + 1] = temp
	return n

def mode(n):
	firstCount = 0
	count = 0
	mode = n[0]
	for i in range(len(n) - 1):
		if(n[i] != n[i+1]):
			firstCount = 0
		else:
			firstCount += 1
			if(firstCount > count):
				count = firstCount
				mode = n[i]
	return mode

n = int(input())
numbers = list(map(int,input().strip().split()))[:n]
mean = mean(numbers)
print("Mean is : " +mean)
sort = sort(numbers)
print(sort)
median = median(sort)
print("Median is : " +median)
mode = mode(sort)
print("Mode is : "  +mode)
