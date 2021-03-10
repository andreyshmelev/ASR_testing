# !/usr/bin/env python3

import socket
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 10001        # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while 1:
        # s.sendall(b'Hello, world')
        # data = s.recv(1024)
        # print('Received', repr(data))
        # time.sleep(1)
        my_str = input("Please enter a string:\n")
        my_str_as_bytes = str.encode(my_str)
        s.sendall(my_str_as_bytes)
        time.sleep(1)

