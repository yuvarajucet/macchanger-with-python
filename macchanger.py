#!/usr/bin/python3

import subprocess,os
from argparse import ArgumentParser

parser = ArgumentParser(description="macchanger [Option] ",usage="python3 macchanger --help",epilog="[ Manual Mode ] python3 macchanger.py -i [interface] -m [XX:XX:XX:XX:XX:XX]")

rparser = parser.add_argument_group("Required Arquments:")

rparser.add_argument('-i','--interface',dest="iface",metavar='',type=str,help="Interface you want to change MAC")
rparser.add_argument('-m','--mac',dest="newmac",metavar='',type=str,help="MAC Address to change [Manual Mode only] ")
parser.add_argument('-s','--show',help="Show available interface and exit",action="store_true")
parser.add_argument('-R','--Random',help="Automaticaly assign Random MAC",action="store_true")
parser.add_argument('-r','--reset',help="Reset to Original MAC",action="store_true")

args = parser.parse_args()


def macchange():
    if ((args.iface) and (args.newmac)):
        subprocess.call(["sudo","ifconfig",args.iface,"down"])
        subprocess.call(["sudo","ifconfig",args.iface,"hw","ether",args.newmac])
        subprocess.call(["sudo","ifconfig",args.iface,"up"])
        subprocess.call(["macchanger","-s",args.iface])
    elif((args.iface) and (args.Random)):
        subprocess.call(["sudo","ifconfig",args.iface,"down"])
        subprocess.call(["sudo","macchanger","-r",args.iface])
        subprocess.call(["sudo","ifconfig",args.iface,"up"])
    elif args.reset:
        subprocess.call(["sudo","ifconfig",args.iface,"down"])
        subprocess.call(["sudo","macchanger","-p",args.iface])
        subprocess.call(["sudo","ifconfig",args.iface,"up"])
    elif args.show:
        print("[:Available Interface:]")
        os.system("sudo netstat -i | awk '{print $1}' > .test.txt")
        os.system("echo ----------------------------------- >> .test.txt")
        subprocess.call(["tail","-n","+3",".test.txt"])
        subprocess.call(["sudo","rm","-rf",".test.txt"])
    else:
        subprocess.call(["python3","macchanger.py","-h"])

if __name__ == '__main__':
    macchange()