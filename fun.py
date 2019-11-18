def f(x,l=[]): 			#In function their is passed two function
	for i in range (x): 	#Loop will run x time which argument will be pass.
		l.append(i*i) 	#According to passed first argument loop will itration and "i 				"multiply with i and it will give output.
	print(l) 	# list will be print.
f(2) 			#output=[0,1]
f(3,[3,2,1]) 		#output=[3,2,1,0,1,4]
f(3,[]) 			#output=[0,1,4]
		
	
