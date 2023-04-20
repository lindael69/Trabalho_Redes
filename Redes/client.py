import socket
import random
import time

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 8888

def generate_combination():
    return ''.join([str(random.randint(0, 9)) for _ in range(random.randint(1, 30))])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

while True:
    combination = generate_combination()
    client_socket.send(combination.encode())
    time.sleep(10)
    response = client_socket.recv(1024).decode()

    if response == 'ok!!':
        print('Combinação recebida pelo servidor com sucesso!')
    else:
        print(f'A combinação "{combination}" é {response}.')

    combination += 'end'
    client_socket.send(combination.encode())

client_socket.close()