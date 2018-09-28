def findminmax(list):
	max=list[0]
	min=list[0]
	#注意list【0】
	for a in list:
		#注意list，不是list（）
			if a<=min:
				min=a
			if a>=max:
				max=a
	return max,min

foundmax,foundmin=findminmax((2,4,1,6))
#注意没有（a,b），后面的（（））
print('max is',foundmax,'min is',foundmin)

