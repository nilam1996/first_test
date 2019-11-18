index=2
num=int(raw_input("Enter your num"))
while(index<num):
	if num%index==0:
		print ("num is not prime")
		break
	index=index+1
else:
	print("num is prime")
