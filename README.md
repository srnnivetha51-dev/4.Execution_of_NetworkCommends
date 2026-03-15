# 4.Execution_of_NetworkCommands
## AIM :Use of Network commands in Real Time environment
## Software : Command Prompt And Network Protocol Analyzer
## Procedure: To do this EXPERIMENT- follows these steps:
<BR>
In this EXPERIMENT- students have to understand basic networking commands e.g cpdump, netstat, ifconfig, nslookup ,traceroute and also Capture ping and traceroute PDUs using a network protocol analyzer 
<BR>
All commands related to Network configuration which includes how to switch to privilege mode
<BR>
and normal mode and how to configure router interface and how to save this configuration to
<BR>
flash memory or permanent memory.
<BR>
This commands includes
<BR>
• Configuring the Router commands
<BR>
• General Commands to configure network
<BR>
• Privileged Mode commands of a router 
<BR>
• Router Processes & Statistics
<BR>
• IP Commands
<BR>
• Other IP Commands e.g. show ip route etc.
<BR>
## PROGRAM
```
SERVER.PY
import socket

server = socket.socket()
server.bind(("localhost", 12346))
server.listen(1)

print("Network Command Server Started...")
print("Waiting for client connection...")

conn, addr = server.accept()
print("Client Connected:", addr)

while True:
    cmd = conn.recv(1024).decode().strip().lower()

    if cmd == "exit" or cmd == "":
        print("Client disconnected")
        break

    if cmd == "1" or cmd == "ifconfig":
        reply = "[INFO] Shows network interface configuration"
    elif cmd == "2" or cmd == "netstat":
        reply = "[INFO] Shows active network connections"
    elif cmd == "3" or cmd == "nslookup":
        reply = "[INFO] Retrieves DNS details of a domain"
    elif cmd == "4" or cmd == "traceroute":
        reply = "[INFO] Displays packet travel path"
    elif cmd == "5" or cmd == "ping":
        reply = "[INFO] Tests host connectivity"
    elif cmd == "6" or cmd == "show ip route":
        reply = "[INFO] Displays routing table entries"
    elif cmd == "7" or cmd == "ipconfig":
        reply = "[INFO] Shows IP configuration details"
    else:
        reply = "[ERROR] Command not recognized"

    conn.send(reply.encode())

conn.close()
server.close()

CLIENT.PY
import socket

client = socket.socket()
client.connect(("localhost", 12346))

print("Connected to Network Command Server")

while True:
    print("\nChoose a Networking Command")
    print("1. ifconfig")
    print("2. netstat")
    print("3. nslookup")
    print("4. traceroute")
    print("5. ping")
    print("6. show ip route")
    print("7. ipconfig")
    print("Type 'exit' to quit")

    cmd = input("Enter choice or command: ")

    client.send(cmd.encode())

    if cmd.lower() == "exit":
        print("Closing connection...")
        break

    reply = client.recv(1024).decode()
    print("Response from Server:", reply)

client.close()
``
## Output

![alt text](<Screenshot 2026-03-15 120914.png>)
![alt text](<Screenshot 2026-03-15 120929.png>)
## Result
Thus Execution of Network commands Performed 
