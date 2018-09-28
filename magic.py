#-*- coding :utf-8 -*-
name=['a','b','c']
newname=[ ]
#要记得定义新列表

def make_great( name  ):
	while name  :
		new_name='thegreat' + name.pop()
		newname.append(new_name)
	return newname
	
newname=make_great(name[:])
#[:]是用副本

def show_magicians (newname):
	for names in newname:
		print ('magician is',names.title())
#for什么就print什么

show_magicians(newname)	



