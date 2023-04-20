import socket

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()

    while True:
        combination = client_socket.recv(1024).decode()

        if len(combination) > 10:
            print('ok!!')
        else:
            parity = 'par' if int(combination) % 2 == 0 else 'ímpar'
            print(f'A combinação "{combination}" é {parity}.')

        combination += 'end'
        client_socket.send(combination.encode())

    client_socket.close()

server_socket.close()