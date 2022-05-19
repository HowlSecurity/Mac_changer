#!/bin/usr/env python

import subprocess
import optparse

def mac_changer(interface, new_mac):
    print("Changing Mac address for" + interface + "to" + new_mac)
    
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig" + interface + "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "down"])

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", help="Specify your interface")
parser.add_option("-m", "--mac", help="New MAC for interface")

interface = input("interface >")
new_mac = input ("New Mac >")

(options, arguments) = parser.parse_args()


mac_changer(options.interface, options.new_mac)


