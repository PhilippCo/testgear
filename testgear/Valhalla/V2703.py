"""Valhalla 2703 AC voltage calibrator"""

import testgear.base_classes as base

class V2703(base.source):
    def set_output(self, voltage=None, current=None, enabled=True, frequency=None, resistance=None, channel=1):
        pass


    def get_output(self):
        """return an object which refelcts the output conditions"""
        obj = base.output_status()
        return obj


#external sense