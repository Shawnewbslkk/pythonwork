def yonghu(name,age,**other):
	#**代表可以随便扩容
	yonghu ={}
#创建字典
	yonghu['name']=name
#字典中key和value对应
	yonghu['age']=age
	for a,b in other.items():
#注意other.item()
		yonghu[a]=b
#新值和对要对应
	return yonghu
#将定义完成的字典返回函数调用



