"""Agilent B2902A Precision Source/Measure Unit"""

#######################################################################################################
# To achieve non-root access to the USB TMC device (Ubuntu 20.04 LTS)
#
# sudo nano /etc/udev/rules.d/50-hpak.rules
#
# copy the following into the file:
# SUBSYSTEMS=="usb", ATTRS{idVendor}=="0957", ATTRS{idProduct}=="8c18", GROUP="users", MODE="0666"
#
# reload the rules:
# sudo udevadm control --reload
#######################################################################################################


import testgear.base_classes as base
import numpy as np

class B2902A(base.source):
    def init(self):
        self.set_timeout(10)
        self.idstr = self.query("*IDN?").strip()

    
    def set_output(self, voltage=None, current=None, enabled=True, frequency=0, resistance=None, fourWire=False, channel=1):
        pass


    def get_output(self):
        """return an object which reflects the output conditions"""
        obj = base.output_status()
        return obj