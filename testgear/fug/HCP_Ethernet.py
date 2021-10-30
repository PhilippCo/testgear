# fug HCP High Voltage Supply controlled via Ethernet

import testgear.base_classes as base

class HCP_Ethernet(base.source):
    pass





 
# # Codeschnipsel von altem Script
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("192.168.137.84", 2101))

# volt = 0
# print(volt)
# amp  = 1e-3
# out  = 1

# s.send(("I"+str(amp)+"\n").encode('utf-8'))
# print(s.recv(4096))

# s.send(bytes("U"+str(volt)+"\n", 'utf-8'))
# print(s.recv(4096))

# s.send(bytes("F"+str(out)+"\n", 'utf-8'))
# print(s.recv(4096))

# s.send(bytes(">m0?\n", 'utf-8'))
# print(s.recv(4096))

# s.send(bytes(">m1?\n", 'utf-8'))
# print(s.recv(4096))
# s.close