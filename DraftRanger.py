##AirRanger Proto - An app to track physicality of a wireless radio in relation to your current location, in human readable formats.
from scapy.all import *
import os
import logging
import subprocess
import time
import sys

iface = input("Enter iface name: ")


def macchange():
    if nmac == 0:
        subprocess.call("macchanger -A" + iface)
    else:
        subprocess.call("ifconfig", iface, "hw", "ether", nmac)
