import subprocess

subprocess.call("ifconfig wlp0s20f3 down", shell=True)
subprocess.call("macchanger -r wlp0s20f3", shell=True)
subprocess.call("ifconfig wlp0s20f3 up", shell=True)