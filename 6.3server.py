import socket
import math
import errno
import sys
from multiprocessing import Process

def process_start(server):
    while True:
            op = server.recv(2048).decode()
            num = server.recv(2048).decode()
            
            if op == '1':
                    cal = math.log(float(num))
                    
            elif op == '2':
                    cal = math.sqrt(float(num))
                    
            elif op == '3':
                    cal = math.exp(float(num))
                    
            elif op == '4':
                    server.close()
                    break
                    
             server.sendall(str(cal).encode())
             
if __name__ == '__main__':
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       host = ''
       port = 4848
       sock.bind((host,port))
       sock.listen(5)
       while True:
                try:
                          server, addr = sock.accept()
                          print('\n Successfully Connected! ')
                          p = Process(target = process_start, args = (server,))
                          p.start()
       sock.close()
