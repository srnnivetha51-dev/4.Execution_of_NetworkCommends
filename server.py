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