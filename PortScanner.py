import socket
import sys
import os
import time

os.system("color a")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = input("Enter the host's ip address you want to scan: ")
print("""
    1. Specific Port
    2. All 1000 Ports
""")
option = int(input("Enter the option you want to use: "))
if option == 1:
    port = int(input("Enter the port: "))
    if s.connect_ex((host,port)):
        print(f"Port {port} is closed")
    else:
        print(f"{port} Port is open")
elif option == 2:
    for port in range(1000):
        if s.connect_ex((host,port)):
            print(f'Port {port} is closed')
        else:
            print(f"{port} Port is open")
        port+=1

# print("Coded by Sahil Singh.")
time.sleep(6)
sys.exit()
            
