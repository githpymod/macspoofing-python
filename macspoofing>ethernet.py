import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("macchanger -r eth0", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
