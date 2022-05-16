try:
	import sys
	import os
	import psutil
except ModuleNotFoundError as e:
	print(e)

def read_file_len(file):
	with open(file ,"r") as f:
		a = [i for i in f.readlines()]
		os.system(f"rm {file}")
		return len(a)

def update():
	file = "update.txt"
	os.system(f"apt list --upgradable >{file}")
	return read_file_len(file)

def installed():
	file = "installed.txt"
	os.system(f"apt list --installed >{file}")
	return read_file_len(file)

def inet():
	file = "ip.txt"
	os.system(f"hostname -I > {file}")
	with open(file ,"r") as f:
		a = f.read().split()[0]
		os.system(f"rm {file}")
		return a

def main(arg):
	if arg == "update": print(update())
	elif arg == "installed": print(installed())
	elif arg == "inet": print(inet())
	elif arg == "cpu": print(f"{psutil.cpu_percent(1)}%")
	elif arg == "ram": print(f"{psutil.virtual_memory()[2]}%")

if __name__ == "__main__":
	main(sys.argv[1])
