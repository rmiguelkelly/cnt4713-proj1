#!/usr/bin/env python3

import sys
import socket
import signal

class file_client:
    def __init__(self):
        
        signal.signal(signal.SIGALRM, self.alarm_handler)
        signal.alarm(10)

        self.socket = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
        self.buffer_size = 64
    
    def create_exception(self, msg):
        ex = Exception()
        ex.message = msg
        return ex

    def alarm_handler(self, signum, frame):
        sys.exit(-2)
        raise self.create_exception("Client Timeout")


    def connect(self, ip = '127.0.0.1', port = 3333):
        
        try:
            self.socket.connect((ip, port))
        except:
            raise self.create_exception("Unable to connect")
        

    def send_file(self, path):
        try:
            file = open(path, "rb")
            fb = file.read(self.buffer_size)
            self.socket.send(fb)

            while (len(fb) > 0):
                fb = file.read(self.buffer_size)
                self.socket.send(fb)

            file.close()
            self.socket.close()
        except:
            raise self.create_exception("Unable to send file")



if __name__ == '__main__':
    client = file_client()


    if (len(sys.argv) <= 3):
        sys.stderr.write("ERROR: format should be: python client.py [HOST] [PORT] [PATH]\n")
        sys.exit(-1)

    try:
        client.connect(sys.argv[1], int(sys.argv[2]))
        client.send_file(sys.argv[3])

        sys.exit(0)

    except Exception as ex:
        sys.stderr.write("ERROR: {}\n".format(ex.message))
        sys.exit(-1)


