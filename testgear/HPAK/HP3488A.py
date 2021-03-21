

class HP3488A(scanner):
    def get_modules(self):
        return ["no card"]
    
    def get_channels(self, modul_idx):
        return []

    def select_channel(self, modul_idx, channel):
        pass

    def set_relay(self,modul_idx, channel):
        pass
    

