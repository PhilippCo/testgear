import testgear.base_classes as base
import numpy as np

class DS2072(base.scope):
    def init(self):
        self.idstr = self.query("*IDN?").strip()


    def set_time_date(self):
        pass


    def screenshot(self, filename="screen.bmp"):
        self.write(":DISPlay:DATA?")
        img = self.resource.read_raw()
        newFile = open(filename, "wb")
        newFile.write(img[11:-1])


    def run(self):
        self.write(":RUN")


    def stop(self):
        self.write(":STOP")

    
    def single(self):
        self.write(":SINGle")

    
    def force_trigger(self):
        self.write(":TFORce")



    def get_waveform(self, channel=1):
        self.write(":WAVeform:SOURce CHAN{0:d}".format(channel))

        self.write(":WAVeform:FORMat BYTE")
        
        self.write(":WAVeform:DATA?")
        samples = int(self.resource.read_bytes(11)[7:])
        data = self.resource.read_bytes(samples)

        xinc  = float(self.query(":WAVeform:XINCrement?"))
        xorig = float(self.query(":WAVeform:XORigin?"))

        yinc  = float(self.query(":WAVeform:YINCrement?"))
        yorig = float(self.query(":WAVeform:YORigin?"))
        yref  = float(self.query(":WAVeform:YREFerence?"))

        s = (np.array(list(data)) - yref - yorig)*yinc 
        t = np.linspace(0, (len(s)-1)*xinc, num=len(s)) + xorig

        return t, s

