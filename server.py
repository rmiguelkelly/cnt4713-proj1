#!/usr/bin/env python3

import sys
import socket
import threading
import signal
import os

class file_server:
    def __init__(self, storage=''):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.file_index = 0
        self.storage_path = storage

    def end(self):
        self.server.close()

    def run(self, ip, port):
        if port >= 0 and port <= 1024:
            callback(False, "Invalid port number supplied")

        self.server.bind((ip, port))
        self.server.listen(10)


        if os.path.exists(self.storage_path) == False:
            os.mkdir(self.storage_path)

        while (True):
            (client, _) = self.server.accept()

            self.file_index += 1

            full_path = os.path.join(self.storage_path, "{}.file".format(self.file_index))

            file = open(full_path, "w+")

            buffer = client.recv(1024)
            file.write(str(buffer))

            while (len(buffer) > 0):
                buffer = client.recv(1024)
                file.write(str(buffer))

            file.close()
            client.close()

def signal_handler(signal, frame):
    fs.end()
    sys.exit(0)

if __name__ == '__main__':
    
    if (len(sys.argv) <= 1):
        sys.stderr.write("ERROR: format should be: python server.py [filepath]\n")
        exit(-1)

    fs = file_server(storage=sys.argv[1])


    signal.signal(signal.SIGINT, signal_handler)
    print 'Press Ctrl+C to end server'

    fs.run('', 3333)


