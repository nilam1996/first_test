index=0
firstNum=0
secondNum=1
thirdNum=0
input=int(raw_input("Enter your num"))
while(index<input):
	thirdNum=firstNum+secondNum
	firstNum=secondNum
	secondNum=thirdNum
	print(firstNum)
	index=index+1

