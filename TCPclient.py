import socket

target_host = "0.0.0.0"
target_port = 9998

#create objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send come data
client.send(b"GET / HTTP/1.1\r\nHi  I TCP Client\r\n\r\n")

#recieve some data
response = client.recv(4096)

print(response.decode)
client.close()