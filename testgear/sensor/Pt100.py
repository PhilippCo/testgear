"""Class to convert Pt100 data from resistance to temperature and the other way around"""

#input and output should be a "reading" object. raise error if input isn't in Ohms

class Pt100():
    def __init__(self):
        self.A = 123
        self.B = 123
        self.C = 123


    def R2temp(self, R, R0=100):
        return 1


    def temp2R(self, temp, R0=100):
        return 1
