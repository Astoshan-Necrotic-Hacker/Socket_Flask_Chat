import socket
import threading

client_num = 0
Disconnect = 'V2VsbCBoZWxsbyB0aGVyZSBteSBmcmllbmQgSSBob3BlIHlvdSBnZXQgdGhpcyByaWdodCBvciBlbHNlIHlvdSB3aWxsIGJlIGRyb3BwZWQuV2VsbCBoZWxsbyB0aGVyZSBteSBmcmllbmQgSSBob3BlIHlvdSBnZXQgdGhpcyByaWdodCBvciBlbHNlIHlvdSB3aWxsIGJlIGRyb3BwZWQu'
super_secret_code_of_doom = 'V2VsbCBoZWxsbyB0aGVyZSBteSBmcmllbmQgSSBob3BlIHlvdSBnZXQgdGhpcyByaWdodCBvciBlbHNlIHlvdSB3aWxsIGJlIGRyb3BwZWQu'
host = '127.0.0.1'
port = 5050
addr = host, port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(addr)

def handle_client():
    connected = True
    while connected:
        test_msg = client.recv(2048)
        test_msg = test_msg.decode('utf-8')
        if test_msg == super_secret_code_of_doom:
            print('[FULL CONNECTION]')
            client.send(bytes('continue', 'utf8'))
            msg_length = client.recv(24)
            client.send(bytes('continue', 'utf-8'))
            msg_length = msg_length.decode('utf-8')
            msg = client.recv(int(msg_length))
            msg = msg.decode('utf-8')
            print(msg)
        elif test_msg == Disconnect:
            client.send(bytes('Thank you for being connected Goodbye', 'utf-8'))
            print('[LEFT] client has left server.')
            break
            
        else:
            client.send(bytes('You are being diconnected for incorrect code.', 'utf-8'))
            print('[INVALID] you need to check in with this connection, because it did not have the right code')
            break

server.listen()
print(f'[LISTENING] on {addr}')
while True:
    client, address = server.accept()
    while True:
        client_num += 1
        the_client = f'{client_num}[CONNECTION] from {address}'
        break
    handle_conn_thread = threading.Thread(target=handle_client)
    handle_conn_thread.start()
    print(the_client)


