#!/usr/bin/python3

import os



#os.system("sudo apt-get install htop")

sudoPassword = '****'

command = 'service syslog-ng restart'

p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
