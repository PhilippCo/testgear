# fug HCP High Voltage Supply controlled via Ethernet

import testgear.base_classes as base

# HV Supply always answers with an error code. 
# Therefore, all communication is via query not write

class HCP_Ethernet(base.source):
    def init(self):
        self.resource.read_termination  = "\r\n"
        self.resource.write_termination = "\r\n"
    

    def ip2visa(self, ip):
        """overload ip2visa for SOCKET communication"""
        return "TCPIP0::{0:s}::2101::SOCKET".format(ip)


    def set_output(self, voltage=None, current=None, enabled=True, frequency=None, resistance=None, channel=1):
        #how to handle negative voltages?

        if enabled:
            self.query("F1")
        else:
            self.query("F0")

        if voltage is not None:
            self.query("U{0:0.3f}".format(voltage))
        
        if current is not None:
            self.query("I{0:0.7f}".format(current))


    def get_output(self, channel=1):
        """return an object which reflects the output conditions"""
        obj = base.output_status()

        if self.query(">DON?").split(":")[1] == '1':
            obj.enabled = True
        else:
            obj.enabled = False

        obj.set_voltage = float(self.query(">s0?").split(":")[1])
        obj.set_current = float(self.query(">s1?").split(":")[1])
        
        obj.voltage = float(self.query(">m0?").split(":")[1])
        obj.current = float(self.query(">m1?").split(":")[1])
        return obj