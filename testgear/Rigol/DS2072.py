import testgear.base_classes as base
import numpy as np
import time

class DS2072(base.scope):
    def init(self):
        self.idstr = self.query("*IDN?").strip()


    def set_time_date(self):
        pass


    def opc(self):
        while True:
            if self.query("*OPC?").strip() == "1":
                break


    def screenshot(self, filename=None):
        if filename is None:
            filename = time.strftime("%Y%m%d-%H%M%S")+"_DS2000.bmp"

        self.write(":DISPlay:DATA?")
        img = self.resource.read_raw()
        newFile = open(filename, "wb")
        newFile.write(img[11:-1])


    def run(self):
        self.write(":RUN")


    def stop(self):
        self.write(":STOP")

    
    def single(self, wait=True, forced=False):
        self.write(":SINGle")
        self.opc()
        if forced:
            self.force_trigger()

        if wait:
            while True:
                if self.query(":TRIGger:STATus?").strip() == "STOP":
                    break

        self.opc()
    

    def force_trigger(self):
        self.write(":TFORce")


    def get_waveform_memory(self, channel=1):
        #use this method to get the whole memory
        mdepth = int(self.query(":ACQuire:MDEPth?"))

        sr = float(self.query(":ACQuire:SRATe?"))

        self.write(":STOP")
        self.write(":WAV:SOUR CHAN{0:d}".format(channel))
        self.write(":WAV:MODE RAW")
        self.write(":WAVeform:POINts {0:d}".format(mdepth))
        self.write(":WAV:RES")
        self.write(":WAV:BEG")

        sample = []

        while True:
            status = self.query(":WAV:STAT?")
            print("lese Daten..")
            self.write(":WAV:DATA?")
            data = self.resource.read_raw()
            sample+= list(data[11:-1])
            print(len(sample))
                
            if status[0] == 'I':
                self.write(":WAV:END")
                break

        yinc  = float(self.query(":WAVeform:YINCrement?"))
        yorig = float(self.query(":WAVeform:YORigin?"))
        yref  = float(self.query(":WAVeform:YREFerence?"))

        xorig = float(self.query(":WAVeform:XORigin?"))

        s = (np.array(sample) - yref - yorig)*yinc
        t = np.linspace(0, (mdepth-1)*1/sr, num=mdepth) + xorig

        return t, s


    def get_waveform(self, channel=1):
        #returns the datapoints from screen
        self.write(":WAVeform:SOURce CHAN{0:d}".format(channel))
        self.write(":WAV:MODE NORM")
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


    def null_offset(self, channel=1):
            vmax = float(self.query(":MEASure:VMAX? CHANnel{0:d}".format(channel)))
            vmin = float(self.query(":MEASure:VMIN? CHANnel{0:d}".format(channel)))

            if vmin+vmax > 1e9:
                return False

            self.write(":CHANnel{0:d}:OFFSet {1:0.6f}".format(channel, -1*np.mean([vmax, vmin]) ) )
            
            return True


    def autoscale(self, channel=1):
        #ToDo: check probe factor
        self.write(":CHANnel{0:d}:DISPlay 1".format(channel))
        self.opc()
        probe = float(self.query(":CHANnel{0:d}:PROBe?".format(channel)))
        self.single(forced=True)

        if float(self.query(":MEASure:VMAX?")) > 1e30:
            #print("out of range")
            self.write(":CHANnel{0:d}:SCALe {1:0.6f}".format(channel, 10 ))
            self.write(":CHANnel{0:d}:OFFSet {1:0.6f}".format(channel, 0 ))
            self.opc()
            self.single(forced=True)
            time.sleep(1)
            
        while True:
            scale = float(self.query(":CHANnel{0:d}:SCALe?".format(channel)))
            vmax = float(self.query(":MEASure:VMAX? CHANnel{0:d}".format(channel)))
            vmin = float(self.query(":MEASure:VMIN? CHANnel{0:d}".format(channel)))
            span = vmax - vmin
            
            if (span * 2 / scale / 8) > 0.2:
                #print("passe Offset an")
                self.write(":CHANnel{0:d}:OFFSet {1:0.6f}".format(channel, -1*np.mean([vmax, vmin]) ) )
            
            #print(vmin + span/2)

            if (span * 2 / scale / 8) > 0.6:
                #print("set fine")
                self.write(":CHANnel{0:d}:SCALe {1:0.6f}".format(channel, span / (8 * 0.8)  ))
                break

            if scale <= (500e-6 * probe):
                #print("limit reached")
                break
                
            self.write(":CHANnel{0:d}:SCALe {1:0.6f}".format(channel, scale/2 ))
            self.single(forced=True)
            
            time.sleep(1)
        
        self.null_offset()