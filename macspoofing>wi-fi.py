import subprocess

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("macchanger -r wlan0", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
