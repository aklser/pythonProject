import socket

client_socket = socket.socket()
ip_port = ("127.0.0.1", 8889)
client_socket.connect(ip_port)
while True:
    client_data = input("请输入要发给服务器的信息：")
    client_socket.send(client_data.encode("utf-8"))
    server_data = client_socket.recv(1024).decode("utf-8")
    if (server_data == "exit") or (not server_data):
        break
    print(f":{server_data}")
client_socket.close()