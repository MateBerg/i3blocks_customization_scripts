#!/bin/python3 
import subprocess 
print("📥 "+subprocess.getoutput("vnstat --oneline -i wlan0").split(';')[5])
