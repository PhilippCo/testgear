"""Fluke 8508A 8.5 digit DMM"""

import testgear.base_classes as base

class F8508A(base.meter):
    def init(self):
        pass

    def get_reading(self):
        return float(self.query("RDG?"))
