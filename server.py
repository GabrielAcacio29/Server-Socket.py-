import socket  # import the socket module for network communication

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # i'm creating a TCP socket
server.bind(('localhost', 8888))

server.listen()
client, endereço = server.accept()

end_connection = False

while not end_connection:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'tt':
        end_connection = True
    else:
        print(msg)
    client.send(input('Mensagem:  ').encode('utf-8'))

client.close()
server.close()

