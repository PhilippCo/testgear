"""HP 3488A Switch Unitexit"""

import testgear.base_classes as base

class HP3488A(base.instrument):
    def init(self):
        self.cards = []
        for slot in range(1, 6):
            cardtype = self.query("CTYPE {0:d}".format(slot)).strip()
            self.cards.append(cardtype)


    def get_errors(self):
        """read errors"""
        return self.query("ERROR")


    def get_modules(self):
        # 44470 Relay Mux
        # 44471 GP Relay
        # 44472 VHF Switch
        # 44473 Matrix Switch
        # 44474 Digital IO
        # 44475 Breadboard - not supported
        return self.cards
    

    def is_module(self, modul_idx, type):
        """test if the card in slot modul_idx is a card of type type"""
        return self.cards[modul_idx].split(' ')[-1] == type


    def reset_module(self, modul_idx):
        self.write("CRESET {0:d}".format(modul_idx))


    def display(self, text):
        """writes a text into the display"""
        self.write("DISP {0:s}".format(text))


    def select_channel(self, modul_idx, channel):
        """select multiplexer channel"""
        self.write("CHAN {0:d}{1:02d}".format(modul_idx, channel))


    def set_relay(self, modul_idx, channel, state):
        """switch relay ON or OFF"""
        if state:
            self.write("CLOSE {0:d}{1:02d}".format(modul_idx, channel))
        else:
            self.write("OPEN {0:d}{1:02d}".format(modul_idx, channel))


    def get_relay(self, modul_idx, channel):
        """status of channel"""
        return self.query("CLOSE {0:d}{1:02d}".format(modul_idx, channel))
 