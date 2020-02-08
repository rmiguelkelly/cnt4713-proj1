#!/usr/bin/env python3

import sys
import socket
import threading
import signal
import os

class file_server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.file_index = 0

    def end(self):
        self.server.close()

    def child_handler(client):
        

    def run(self, ip, port):
        if port >= 0 and port <= 1024:
            callback(False, "Invalid port number supplied")

        self.server.bind((ip, port))
        self.server.listen(10)

        while (True):
            (client, _) = self.server.accept()
            self.file_index += 1

            file = open("/Users/ronankelly/Desktop/netcentric/cnt4713-proj1/{}.file".format(self.file_index), "w+")

            buffer = client.recv(1024)
            file.write(str(buffer))

            while (len(buffer) > 0):
                buffer = client.recv(1024)
                file.write(str(buffer))


            file.close()
            client.close()
    

fs = file_server()

def signal_handler(signal, frame):
    fs.end()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print 'Press Ctrl+C to end server'

fs.run('', 3333)
