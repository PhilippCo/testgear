"""Espec Thermal Chamber"""

import requests
import json

class PU4J():
    def __init__(self, ip):
        self.ip = ip

    
    def set_temp(self, temp):
        form_data = {
            "save": "save",
            "saveSigs": "",
            "temp_setpoint": "15.0",
            "humi_setpoint": "undefined",
            "refrigeration_control": "REF1",
            "_":""
        }

        form_data["temp_setpoint"] = "{0:0.1f}".format(temp)

        session = requests.Session()
        session.post(url="http://{0:s}/app/app.app".format(self.ip), data=form_data)
        session.close()


    def get_temp(self):
        session = requests.Session()
        response = session.get("http://10.33.46.47/app/app.app?temp=%5B%5D")
        data = json.loads(response.text)["temp"]
        setpoint = data["target"]
        measured = data["monitored"]
        return {"setpoint": setpoint, "measured": measured}


    def __repr__(self):
        string = "============ Testgear Instrument ============\n"
        string += "Class:\t\t{}\n".format(type(self).__name__)
        string += "IP Address:\t{}\n".format(self.ip)
        #string += "ID String:\t{}\n".format(self.idstr)
        #string += "Timeout:\t{0:0.3f} s\n".format(self.resource.timeout/1000)

        return string


    def is_type_of(self, insttype):
        """Check if class is of a specific type"""
        if type(self).__name__ == insttype:
            return True
        else:
            return False