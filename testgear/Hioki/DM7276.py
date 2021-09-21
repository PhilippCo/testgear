"""Hioki DM7276 7.5 digit DVM"""

import testgear.base_classes as base

class DM7276(base.meter):
    def init(self):
        self.lasttemp = -1

        self.set_timeout(10)
        self.resource.read_termination  = "\r\n"
        self.resource.write_termination = "\r\n"

        self.write("*RST")
        self.idstr = self.query("*IDN?").strip()
        self.write(":TRIG:SOUR EXT")
        self.write(":INITiate:CONTinuous OFF")
        self.write(":SYST:COMM:FORM FLOAT")


    def ip2visa(self, ip):
        """overload ip2visa for SOCKET communication"""
        return "TCPIP0::{0:s}::23::SOCKET".format(ip)


    def set_time_date(self):
        """set time and date to compute date"""
        pass

    
    def scale(self, offset=0, gain=1):
        if offset == 0 and gain == 1:
            pass #scaling ausschalten
        else:
            pass

    def get_temp(self):
        return self.lasttemp


    def screenshot(self, filename=None):
        self.write(":HCOPy:SDUMp:DATA?")
        img = self.resource.read_raw()
        newFile = open("screen.bmp", "wb")
        newFile.write(img[8:-2])


    def get_reading(self, channel=None):
        self.write(":READ? TEMP")
        value, temp = self.query("*TRG").split(",")
        self.lasttemp = float(temp)
        return float(value)

    
    def conf_function_DCV(self, mrange=10, nplc=100, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange
        NPLC 0.02..100
        """
        self.write(":VOLTAGE:DC:RANGE {0:0.3f}".format(mrange))
        self.write(":SENSe:VOLTage:DC:NPLCycles {0:0.2f}".format(nplc))

        if HiZ:
            self.write("SENSe:VOLTage:DC:IMPedance:AUTO ON")
        else:
            self.write("SENSe:VOLTage:DC:IMPedance:AUTO OFF")