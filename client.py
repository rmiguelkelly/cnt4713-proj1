#!/usr/bin/env python3

import sys
import socket

class file_client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
        self.on_connect = None
        self.on_error = None
        self.on_file_send = None

    def connect(self, ip = '127.0.0.1', port = 3333):
        try:
            self.socket.connect((ip, port))
        except:
            self.on_error("Error connecting to server")
        

    def send_file(self, path):
        try:
            file = open(path, "r")
            bytes_sent = 0
            fb = file.read(1024)
            self.socket.send(fb)
            bytes_sent += len(fb)

            while (len(fb) > 0):
                fb = file.read(1024)
                bytes_sent += len(fb)
                self.socket.send(fb)
            file.close()
            if self.on_file_send is callable:
                self.on_file_send(bytes_sent)
        except:
             self.on_error("Socket is not connected")

def client_error(m):
    sys.stderr.write("ERROR: {}\n".format(m))

def client_connect_success(m):
    print(m)

def client_did_send_file(size):
    print("{} bytes sent to server".format(size))

if __name__ == '__main__':
    client = file_client()

    """Set up event handlers"""
    client.on_connect = client_error
    client.on_error = client_error

    """Attempt to connect"""
    client.connect()

    """Send file to server"""
    client.send_file('/Users/ronankelly/Desktop/data2.txt')
