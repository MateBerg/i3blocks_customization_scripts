#!/bin/python
import subprocess 

percent = subprocess.getoutput("xbacklight -get")
per2 = int(percent)

if per2 <= 5 :
	per3 = subprocess.getoutput("xbacklight -set 5")
	per2 = 5

per3 = str(per2)

print ("🔆 "+per3+"%")	