"""Fluke 5730A Multifunction Calibrator"""

import testgear.base_classes as base

class F5730A(base.source):

    def set_output(self, voltage=None, current=None, enabled=True, frequency=None, resistance=None, channel=1):
        pass

    
    def get_output(self):
        """return an object which reflects the output conditions"""
        obj = base.output_status()

        return obj