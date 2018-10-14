import os
from datetime import datetime
from netmiko import ConnectHandler
import re

#This script will SSH into specified device with the assigned parameters and copy the running configuration
#into a folder located in the root directory of where this file was written, This requires human intervention


ipAddr = input("Enter IP: ")
usr = input("Enter username: ")
pwd = input("Enter password: ")
pwd1 = input("Enter secret: ")
test = "show run"
device = ConnectHandler(device_type='cisco_ios', ip=ipAddr, username=usr, password=pwd, secret=pwd1)
name_of_device = device.find_prompt()
print(device.find_prompt())  # This is useful to verify our ssh connection by checking the prompt of the device
realname = re.sub('>', "", name_of_device)
shrun = device.send_command(test)
print(shrun)
filename = ("{0}-{1}.txt".format(datetime.now().strftime("%H-%M-%S-"), name_of_device))
# with open(os.path.join('/Users/Utente/Backup', filename), "w") as file:
# file.write(shrun)
# file.close()
# Simple write text file function


def writeTextFile(_name, _text):
    #takeme = re.sub('\\', " ", _name)
    fileName = ("{0}.txt".format(_name))
    file = open(fileName, 'w')
    file.write(_text)
    file.close()


try:
    fileName = ("{0}_{1}".format(realname, datetime.now().strftime('%d-%m-%Y')))
    writeTextFile(os.path.join('backups', fileName), shrun)  # By not specifying path, it will look into the root directory of where this file is being written from and look into backups folder
except OSError as err:
    print("OS Error: {0}".format(err))
