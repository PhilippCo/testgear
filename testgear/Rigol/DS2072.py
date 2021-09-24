import testgear.base_classes as base

class DS2072(base.scope):
    def init(self):
        self.idstr = self.query("*IDN?").strip()


    def set_time_date(self):
        pass


    def screenshot(self, filename=None):
        self.write(":DISPlay:DATA?")
        img = self.resource.read_raw()
        newFile = open("screen.bmp", "wb")
        newFile.write(img[11:-1])


