import numpy as np
import socket
import time


#ToDo: adapt class to PyVISA and similar interface

class hvmeas():
    def __init__(self, visastr=None, gpib=None, gwip=None, ip=None, serial=None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, 5005))


    def sar(self):
        self.sock.send(("sar").encode('utf-8'))
        self.sock.recv(4096)

        while True:
            time.sleep(1)
            self.sock.send(("status?").encode('utf-8'))
            status = float(self.sock.recv(4096))
            if status == 0:
                break


    def get_adc(self):
        self.sock.send(("adc_raw?").encode('utf-8'))
        return float(self.sock.recv(4096))


    def get_dac(self):
        self.sock.send(("dac_raw?").encode('utf-8'))
        return float(self.sock.recv(4096))


    def get_volt(self):
        self.sock.send(("volt?").encode('utf-8'))
        return float(self.sock.recv(4096))


    def reset_stat(self):
        self.sock.send(("reset").encode('utf-8'))
        self.sock.recv(4096)


    def close(self):
        self.sock.send(("quit").encode('utf-8'))
        self.sock.close


    def get_reading(self, channel=None):
        return self.get_volt()
