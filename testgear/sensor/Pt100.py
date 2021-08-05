"""Class to convert Pt100 data from resistance to temperature and the other way around"""

from scipy import optimize
import numpy as np

#input and output should be a "reading" object. raise error if input isn't in Ohms

class Pt100():
    def __init__(self):
        self.__A = 3.9083 * 1e-3
        self.__B = -5.775 * 1e-7
        self.__C = -4.183 * 1e-12


    def __R2temp(self, res, R0=100):
        A = self.__A
        B = self.__B
        return (( (A**2)*R0 + 4*B*res - 4*B*R0)**0.5 - (A*(R0**0.5)))   / (2*B*(R0**0.5))


    def temp2R(self, t, R0=100):
        A = self.__A
        B = self.__B
        C = np.where( t < 0, self.__C, 0)
    
        return R0 * (1 + A * t + B * t**2 + C * (t - 100) * t**3)


    def R2temp(self, res, R0=100):
        return optimize.newton(lambda t: self.temp2R(t, R0)-res, self.__R2temp(res))
