n = int(input())
x = list(input())[:n]
if(((ord(x[0])) > 96) and ((ord(x[0])) < 123)):
	for j in range(1,n):
		if((((ord(x[j])) > 48) and ((ord(x[j])) < 60)) or (ord(x[j]) != (ord(x[j-1]) + 1))):
			print("Wrong Format")
			break
		else:
			count = 0
			for i in range(1,n):
				if((((ord(x[i])) > 96) and ((ord(x[i])) < 123)) and (ord(x[i]) == (ord(x[i-1]) + 1))):
					count += 1
			if(count == (n-1)):
				print("All Cool")	
				break
			
elif(((ord(x[0])) > 48) and ((ord(x[0])) < 60)):
	for j in range(1,n):
		if((((ord(x[j])) > 96) and ((ord(x[j])) < 123)) or (ord(x[j]) != (ord(x[j-1]) + 1))):
			print("Wrong Format")
			break
		else:
			count = 0
			for i in range(1,n):
				if((((ord(x[i])) > 48) and ((ord(x[i])) < 60)) and (ord(x[i]) == (ord(x[i-1]) + 1))):
					count += 1
			if(count == (n-1)):
				print("All Cool")	
				break
				
