from netmiko import ConnectHandler
import os
import json

########################################
#Simple script that creates n loopbacks#
#with n IP addresses provided          #
#in a text file                        #
########################################


class Connection (object):
    def __init__(self, device_details):
        self.connection = ConnectHandler(**device_details)
        self.connection.enable()
        
        
    def createLoopback(self,interfacenumber, loopback):
        config_set = """
         interface loopback{0}
         ip address {1}  """
        createloopback =self.connection.send_config_set(config_set.format(interfacenumber,loopback))
        
                                                    
        
                                                            
device =  {'device_type': 'cisco_ios',
           'ip': '192.168.1.2' ,
           'secret' : 'cisco',
           'password' :'cisco',
           'username' :'cisco'
           }

session = Connection(device)                                                   
with open("IPs.txt" , "r") as f:
    file = f.read()
    
ip = file.split("\n")
for count,ipz in enumerate(ip):
    print("Configuring loopback {0}...".format(count))
    session.createLoopback(count,ipz[count])
 



###################################
#                                 #
#   Wrote by Delio Innamorati.    #
#                                 # 
###################################
