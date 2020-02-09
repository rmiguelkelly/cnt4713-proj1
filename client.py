#!/usr/bin/env python3

import sys
import socket

class file_client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
        self.on_connect = None
        self.on_error = None

    def connect(self, ip = '127.0.0.1', port = 3333):
        try:
            self.socket.connect((ip, port))
        except:
            self.on_error("Error connecting to server")
        

    def send_file(self, path):
        try:
            file = open(path, "r")
            fb = file.read(1024)
            self.socket.send(fb)


            while (len(fb) > 0):
                fb = file.read(1024)
                self.socket.send(fb)
                
            file.close()
        except:
             self.on_error("Socket is not connected")

def client_error(m):
    sys.stderr.write("ERROR: {}\n".format(m))
    exit(-1)

def client_connect_success(m):
    print("Connected Successfully")


if __name__ == '__main__':
    client = file_client()

    """Set up event handlers"""
    client.on_connect = client_error
    client.on_error = client_error

    if (len(sys.argv) <= 3):
        sys.stderr.write("ERROR: format should be: python client.py [HOST] [PORT] [PATH]\n")
        exit(-1)

    """Attempt to connect"""
    client.connect(sys.argv[1], int(sys.argv[2]))

    """Send file to server"""
    client.send_file(sys.argv[3])
