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
        self.buffer_size = 64

    def end(self):
        self.server.close()

    

    def handle_client_connection(self, client, path):
        file = open(path, "wb")    

        buffer = client.recv(self.buffer_size)
        file.write(buffer)

        while (len(buffer) > 0):
            buffer = client.recv(self.buffer_size)
            file.write(buffer)

        file.close()
        client.close()

    def run(self, ip, port):

        self.server.bind((ip, port))
        self.server.listen(10)

        if os.path.exists(self.storage_path) == False:
            os.mkdir(self.storage_path)

        while (True):
            (client, _) = self.server.accept()
            self.file_index += 1
            full_path = os.path.join(self.storage_path, "{}.file".format(self.file_index))
            c_thread = threading.Thread(target=self.handle_client_connection, args=(client, full_path))
            c_thread.daemon = True
            c_thread.start()

def signal_handler(signal, frame):
    fs.end()
    sys.exit(0)

if __name__ == '__main__':
    
    if (len(sys.argv) <= 2):
        sys.stderr.write("ERROR: format should be: python server.py [PORT] [PATH]\n")
        sys.exit(-1)

    fs = file_server(storage=sys.argv[2])

    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C to end server')

    port = int(sys.argv[1])

    if (port <= 0 or port >= 65535):
        sys.stderr.write("ERROR: Port should be between 0 and 65535\n")
        exit(-1)

    fs.run('', port)


