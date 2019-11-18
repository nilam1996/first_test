index=0
sum=0
input=int(raw_input("Enter your num"))
num=input
while(num>0):
	reminder=num%10
	sum+=reminder**3
	num//=10
if sum==input:
	print("number is armstrong")
else:
	print("number is not armstrong")
	
