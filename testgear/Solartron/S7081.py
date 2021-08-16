
#rudimentär und ungetestet

import testgear.base_classes as base

class S7081(base.meter):
    def init(self):
        self.write("DELIMT=END")
        self.write("Output, GP-IB, ON")
        self.write("NINES = 8")
        self.write("MEASURE, CON")

        self.set_timeout(70)


    def get_reading(self, channel):
        return float(self.read())