import sys
import os
import psutil

def argv() -> list:
	l= []
	args = sys.argv
	for i in range(len(args)):
		if i != 0:
			l.append(args[i])
	return l

def read_file(file):
	f = open(file ,"r")
	counter = 0
	for i in f:
		counter += 1
	return counter

def exec(li):
	command = li[0]
	file = li[1]
	os.system(command +file)
	count = read_file(file)
	print(count - 1)
	os.system("rm " +file)

def updates():
	file = "updates.txt"
	command = "apt list --upgradable > "
	return [command ,file]

def installed():
	file = "installed.txt"
	command = "apt list --installed > "
	return [command ,file]

def inet():
	file = "ip.txt"
	os.system("ip a >" + file)
	f = open(file ,"r")
	ip = []
	for i in f:
		if "inet" in i and "enp5s" in i:
			first_index = i.index("1")
			for v in range(14):
				ip.append(i[first_index])
				first_index += 1
	ip = "".join(ip)
	os.system("rm " +file)
	return "inet: " + str(ip)

def cpu():
	return str(psutil.cpu_percent(1)) + "%"

def ram():
	return str(psutil.virtual_memory()[2]) + "%"

def main(argv):
	command = argv[0]
	if command == "update": exec(updates())
	elif command == "installed": exec(installed())
	elif command == "inet": print(inet())
	elif command == "cpu": print(cpu())
	elif command == "ram": print(ram())
	else: print(False)

if __name__ == "__main__":
	main(argv())
