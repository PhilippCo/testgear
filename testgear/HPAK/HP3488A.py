
import testgear.base_classes as base

class HP3488A(base.scanner):
    def get_modules(self):
        return ["no card"]
    
    def get_channels(self, modul_idx):
        return []

    def select_channel(self, modul_idx, channel):
        pass

    def set_relay(self,modul_idx, channel):
        pass
    

