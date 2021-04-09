"""Siglent SDG1025 Signal Generator"""

#######################################################################################################
# To achieve non-root access to the USB TMC device (Ubuntu 20.04 LTS)
#
# sudo nano /etc/udev/rules.d/50-siglent.rules
#
# copy the following into the file:
# SUBSYSTEMS=="usb", ATTRS{idVendor}=="f4ed", ATTRS{idProduct}=="ee3a", GROUP="users", MODE="0666"
#
# reload the rules:
# sudo udevadm control --reload
#######################################################################################################


# 'USB0::62701::60986::SDG00004131329::0::INSTR'

import testgear.base_classes as base

class SDG1025(base.source):
    def reset(self):
        self.write("*RST")


    def set_output(self, state, channel=1):
        if state:
            self.write("C{0:d}:OUTP ON".format(channel))
        else:
            self.write("C{0:d}:OUTP OFF".format(channel))


    def set_output_level(self, Vpp=None, Vrms=None, Offset=None, Vhigh=None, Vlow=0, channel=1):
        if Vpp is not None:
            self.write("C1{0:d}:BSWV AMP,{1:f}".format(channel, Vpp))
        elif Vhigh is not None:
            self.write("C1{0:d}:BSWV HLEV,{1:f}".format(channel, Vhigh))
            self.write("C1{0:d}:BSWV LLEV,{1:f}".format(channel, Vlow))
        elif Vrms is not None:
            #rms = 1 #add calculation of rms based on amp and offset
            print("not supported yet!")
            self.write("C1{0:d}:BSWV AMP,{1:f}".format(channel, 2*(2**0.5)*Vrms))

        if Offset is not None:
            self.write("C1{0:d}:BSWV OFST,{1:f}".format(channel, Offset))



    def set_frequency(self, frequency, channel=1):
        self.write("C1{0:d}:BSWV FRQ,{1:f}".format(channel, frequency))


    def set_period(self, period, channel=1):
        self.write("C1{0:d}:BSWV PERI,{1:f}".format(channel, period))


    def set_waveform(self, waveform, channel=1):
        """set waveform type: SINE, SQUARE, RAMP, PULSE, NOISE, ARB, DC, PRBS"""
        self.write("C1{0:d}:BSWV WVTP,{1:s}".format(channel, waveform))


    def set_dutycyle(self, dc, channel=1):
        self.write("C1{0:d}:BSWV DUTY,{1:f}".format(channel, dc))


    def conf_output(self, load_50R=False, invert_polarity=False, channel=1):
        if load_50R:
            load_str = "50"
        else:
            load_str = "HZ"

        if invert_polarity:
            pol_str = "INVT"
        else:
            pol_str = "NOR"

        self.write("C{0:d}:OUTP LOAD,{1:s},PLRT,{2:s}".format(channel, load_str, pol_str))

