#!/bin/python3

import subprocess 

used = str(subprocess.getoutput("duf -output used -style ascii / | tail -2").replace("-","").replace("+","").replace("|",""))
size = str(subprocess.getoutput("duf -output size -style ascii / | tail -2").replace("-","").replace("+","").replace("|",""))

used = used.replace("\n","").replace(" ","")
size = size.replace("\n","").replace(" ","")

print("💾 "+used+"-"+size)