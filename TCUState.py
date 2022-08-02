# SSH toutorial
# https://www.devdungeon.com/content/python-ssh-tutorial

#from paramiko import SSHClient
import paramiko
import configparser
import errno
from pathlib import Path
import subprocess
import sys
import os
import logging



def TCUState_config_create(config_file_name):
    TCUState_config = configparser.ConfigParser()
    TCUState_config['debug'] = {}
    TCUState_config['debug']['level'] = "critical"

    TCUState_config['TCU'] = {}
    TCUState_config['TCU']['IP_ADDRESS'] = "192.168.8.2"

    TCUState_config['TCUState'] = {}
    TCUState_config['TCUState']['output_filename'] = "TCUState.txt"

    TCUState_config['files'] = {}
    TCUState_config['files']['logfile'] = "TCUStateDebug.log"
    TCUState_config['files']['output_filename'] = "TCUState.txt"
    """
	in the ADB_Supervision.ini in small letters
	!Level!		!When it’s used!
	DEBUG		Detailed information, typically of interest only when diagnosing problems.
	INFO		Confirmation that things are working as expected.
	WARNING		An indication that something unexpected happened, or indicative of some
				problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
	ERROR		Due to a more serious problem, the software has not been able to perform some function.
	CRITICAL	A serious error, indicating that the program itself may be unable to continue running.
	"""
    try:
        with open(config_file_name, 'w') as configfile:
            TCUState_config.write(configfile)
    except:
        print(str(errno))
def TCUState_wait_for_TCU():
    dot_counter=0
    TCU_IP_ADDRESS=TCUState_config['TCU']['IP_ADDRESS']
    output = ""
    print("try to reach TCU on " + str(TCU_IP_ADDRESS))
    while output=="":
        print("." , end="")
        dot_counter += 1
        try:
            #print("check")
            output = ""
            output = subprocess.check_output(["ping", str(TCU_IP_ADDRESS), "-n", "1", "-w", "5"], shell=True, stderr=subprocess.STDOUT)
            #print(output)
            # 0% Verlust
        except:
            stateHCP5ADBDEBUG = "searching"
            adb_output = ""
        if(dot_counter == 10):
            print("")
            print("USB-cable connected?")
        if(dot_counter == 20):
            print("")
            print("Driver for NDIS installed?")
        if(dot_counter == 30):
            print("")
            print("Has your NDIS adapter a IP-address ?")
        if(dot_counter == 40):
            print("")
            print("Use for example the IP-address 192.169.8.5 !")
        if(dot_counter == 50):
            print("")
            print("Don't use the IP-address 192.169.8.2 !")
        if(dot_counter == 50):
            print("")
            print("Is your USB-cable broken?")
        if(dot_counter == 60):
            print("")
            print("Is the TCU connected to KL30 and KL31?")
        if(dot_counter == 70):
            print("")
            print("Press CTRL+c to exit")

#Check if TCUState.ini exists if not create it
TCUState_config_file = Path("TCUState.ini")
if TCUState_config_file.is_file():
    pass
else:  # create file
    print(TCUState_config_file)
    TCUState_config_create(TCUState_config_file)

try:
    TCUState_config = configparser.ConfigParser()
    TCUState_config.read('TCUState.ini')
    if(TCUState_config.has_section('debug') == False):
        print("Can't use TCUState.ini -> exit")
        exit(-20)
except:
    exit(-20)

TCUState_wait_for_TCU()

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------


print ('connecting')
client = paramiko.SSHClient()
policy = paramiko.AutoAddPolicy()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=str(TCUState_config['TCU']['IP_ADDRESS']), username='pi', password='raspberry')
#client.exec_command('cat /etc/hosts')
channel = client.invoke_shell()
client.stdin = channel.makefile('wb')
client.stdout = channel.makefile('r')
client.stdin.write('cat /etc/hosts\n')
client.stdin.write('cat /etc/hosts\n')
client.stdin.write('cat /etc/hosts\n')
#stdin, stdout, stderr = client.exec_command('cat /etc/hosts')
#stdin, stdout, stderr = client.exec_command('cat /etc/hosts')
#while True:
#  if channel.exit_status_ready():
#    if channel.recv_ready():
#      print ('done generating graph')
#      break
    #temp=str(channel.recv(100))
    #if(temp!=""):
while(True):
    stdoutLines = client.stdout.readline()
    if stdoutLines!='':
        print (stdoutLines,end='')
while (True):
    while not stdout.channel.exit_status_ready():
        if stdout.channel.recv_ready():
            stdoutLines = stdout.readlines()
            print(str(stdoutLines))
            #exit(55)
            #output=output+temp
            #print(output, end="")
            #exit(55)

#if(output!=""):
    #    print(str(output).encode('utf-8'))
print ('closing ssh channel')
client.close()















client = paramiko.SSHClient()
try:
    client.load_system_host_keys(filename='.\\known_hosts')
except:
    print(str( errno.errorcode ))
    print(str( errno.EPERM ))
    print("Error")
policy = paramiko.AutoAddPolicy()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=str(TCUState_config['TCU']['IP_ADDRESS']), username='root', password='')





# Example command:
stdin, stdout, stderr = client.exec_command('cd /usr')
if (stdout.channel.recv_exit_status()==0):
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))

stdin, stdout, stderr = client.exec_command('cat /etc/hosts')
if (stdout.channel.recv_exit_status()==0):
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))

stdin, stdout, stderr = client.exec_command('cli-connect telematics-services')
stdin.close()
while (1==1):
    for line in iter(lambda: stdout.readline(2048), ""):
        print(line, end="")
while (1==1):
    a=str(stdout.readlines())
    if (a!=""):
        print(a)
    a=str(stdin.readline())
    if (a!=""):
        print(a)
if (stdout.channel.recv_exit_status()==0):
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))

stdin, stdout, stderr = client.exec_command('/ecall/status')
if (stdout.channel.recv_exit_status()==0):
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))

while (1==1):
    a=str(stdout.readlines())
    if (a!=""):
        print(a)
    a=str(stdin.readline())
    if (a!=""):
        print(a)





stdin.close()
stdout.close()
stderr.close()


client.close()
client.save_host_keys('.\\known_hosts')
