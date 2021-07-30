import socket
import threading
import sys


disconnect = 'V2VsbCBoZWxsbyB0aGVyZSBteSBmcmllbmQgSSBob3BlIHlvdSBnZXQgdGhpcyByaWdodCBvciBlbHNlIHlvdSB3aWxsIGJlIGRyb3BwZWQuV2VsbCBoZWxsbyB0aGVyZSBteSBmcmllbmQgSSBob3BlIHlvdSBnZXQgdGhpcyByaWdodCBvciBlbHNlIHlvdSB3aWxsIGJlIGRyb3BwZWQu'
secret_conn_code = 'V2VsbCBoZWxsbyB0aGVyZSBteSBmcmllbmQgSSBob3BlIHlvdSBnZXQgdGhpcyByaWdodCBvciBlbHNlIHlvdSB3aWxsIGJlIGRyb3BwZWQu'
host = '127.0.0.1'
port = 5050
addr = host, port
#msg_byte_amount = 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def get_byte_amount(x):
    byte_amount = sys.getsizeof(x)
    return byte_amount

def THESENDER():
    while True:
        client.send(bytes(secret_conn_code, 'utf-8'))
        msg = client.recv(64)
        if msg.decode('utf-8') == 'continue':
            msg_to_send = sys.argv[1]
            print('Ready to send byte amount')
            byte_amount = get_byte_amount(msg_to_send)
            client.send(bytes(str(byte_amount), 'utf-8'))
            next_msg = client.recv(64)
            if next_msg.decode('utf-8') == 'continue':
                if msg_to_send == '/disconnect':
                    client.send(bytes(disconnect, 'utf-8'))
                else:
                    client.send(bytes(msg_to_send, 'utf-8'))
            else:
                print(msg)
                break
        else:
            print(msg)
            break

def THERECIEVER():
    while True:
        msg_recieve = client.recv(1024)
        print(msg_recieve)


THESENDER()
recive = threading.Thread(target=THERECIEVER)

