import socket

sv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sv_ipport = ("0.0.0.0", 8889)
sv_socket.bind(sv_ipport)
sv_socket.listen(5)
print("等待客户端")
server_socket, addr = sv_socket.accept()
while True:
    client_data = server_socket.recv(1024).decode("utf-8")
    if (client_data == "exit") or (not client_data):
        break
    print(f"收到的信息是{client_data}")
    server_data = input("要发送的信息是：")
    server_socket.send(server_data.encode("utf-8"))
server_socket.close()
