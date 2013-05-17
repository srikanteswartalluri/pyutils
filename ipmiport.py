#!/usr/bin/python2.7
import os
ipmi_addr = raw_input("enter the ipmi address:")
ipmi_addr.rstrip()
os.system("ipmitool -Uroot -Pcalvin -H%s chassis bootdev pxe;ipmitool -Uroot -Pcalvin -H%s chassis power cycle" % (ipmi_addr, ipmi_addr))