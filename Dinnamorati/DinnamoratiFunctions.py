#################################################################
#This is a little network automation library used in conjunction#
#with Netmiko.It contains functions that help you               #
#automate basic-intermediate tasks of a network                 #
#################################################################

from netmiko import ConnectHandler
import zipfile
import os
import time
import csv
import textfsm
from pprint import pprint
from datetime import datetime
import shutil


def connectSSH (device):
    session = ConnectHandler(**device)
    return session


def get_version(session):
    session.enable()
    version = session.send_command('show version')
    output = textfsm_extractor('cisco_ios_show_version.template',version)
    pprint (output)
    
def get_show_ip_int_brief (session):
    show_ip_int_brief = session.send_command('show ip interface brief')
    output = textfsm_extractor('cisco_ios_show_ip_interface_brief.template',show_ip_int_brief)
    pprint (output)

def get_show_ip_route (session):
    session.enable()
    show_ip_route = session.send_command ('show ip route')
    output = textfsm_extractor('cisco_ios_show_ip_route.template',show_ip_route)
    pprint (output)

def configure_management_ip (interface, ip, subnet_mask,session):
    session.enable()
    config_set="""
             interface loopback{0}
             ip address {1} {2}"""
    ip_management = session.send_config_set(config_set.format(interface ,ip, subnet_mask))
    pprint(ip_management)
    
def create_vlan (vlan_id, vlan_name, session):
    session.enable()
    config_set="""
               vlan {0}
               name {1}
               """
    create = session.send_config_set(config_set.format(vlan_id, vlan_name))

def get_hostname(session):
     session.enable()
     return(session.find_prompt().replace('#', ''))
        
   
def get_running_configuration(session):
    session.enable()
    running_configuration = session.send_command("show running-config")
    session.exit_enable_mode()
    #splitConfigFile = running_configuration.split('\n')
    
    try:
         if(os.path.exists('backups')):
             fileName = ("{0}_{1}".format(get_hostname(session),datetime.now().strftime('%d-%m-%Y')))
             writeTextFile(os.path.join('backups', fileName),  running_configuration)
   

         else:
             os.mkdir('backups')
             fileName = ("{0}_{1}".format(get_hostname(session),datetime.now().strftime('%d-%m-%Y')))
             writeTextFile(os.path.join('backups', fileName),  running_configuration)
    except OSError as err:
        print("OS Error: {0}".format(err))
         
#################################################
# This textfsm function was taken from NAPALM	#
# https://napalm-automation.net/		#
# https://github.com/napalm-automation/napalm   #
#################################################
def textfsm_extractor(template_name, raw_text):
    textfsm_data = list()
    fsm_handler = None

    template_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),'textfsm_templates'))
    template_path = '{0}/{1}'.format(template_directory, template_name)

    with open(template_path) as f:
        fsm_handler = textfsm.TextFSM(f)

        for obj in fsm_handler.ParseText(raw_text):
            entry = {}
            for index, entry_value in enumerate(obj):
                entry[fsm_handler.header[index].lower()] = entry_value
            textfsm_data.append(entry)

        return textfsm_data

##############################################
#Simple write text file function
def writeTextFile(_name, _text):
    fileName = ("{0}.txt".format(_name))
    file = open(fileName,'w')
    file.write(_text)
    file.close()
##############################################

def ZipBackups():
   
    shutil.make_archive('ZippedBackups', 'zip', 'backups') #This is used to create a zip with the files in the third parameter, first is the name you want to give and zip is the type.
    
    
    
    





