#!/usr/bin/python3
from tkinter import *
from tkinter import simpledialog
import os,time,subprocess,webbrowser


#Functionss.-------
os.system("touch .log.txt")
def follow():
    out = subprocess.call(["firefox","https://yuvarajucet.github.io"])
    if(out == 0 ):
        print("----> Follow Me On Social Media <-----")
    else:
        os.system("chromium --no-sandbox https://yuvarajucet.github.io")
        print("----> Follow Me One Social Media <-----")
def show_mac():
    interface = simpledialog.askstring(title="Interface",prompt="Choose interface")
    check = subprocess.call(["sudo","ifconfig",interface])
    if(check == 0):
        mac = subprocess.check_output(['macchanger','-s',interface])
        test.insert(END,"[+] Your curent MAC\n")
        test.insert(END,"-------------------\n")
        test.insert(END,mac)
    else:
        test.insert(END,"[-] Interface Not found!")

def show_interface():
    os.system("netstat -i | awk '{print $1}' > .log.txt")
    os.system("echo ----------------------- >> .log.txt")
    inter = subprocess.check_output(["tail","-n","+3",".log.txt"]) 
    test.insert(END,"[+] Availabe Interface\n")
    test.insert(END,"-----------------------\n")
    test.insert(END,inter)

def manual_mac():
    interface = simpledialog.askstring(title="Interface",prompt="Choose interface to change MAC")
    check = subprocess.call(["sudo","ifconfig",interface])
    if(check == 0):
        newmac = simpledialog.askstring(title="MAC Address",prompt="Enter New MAC address")
        test.insert(END,"\n\n[+] Changing to New MAC..\n")
        subprocess.call(["sudo","ifconfig",interface,"down"])
        subprocess.call(["sudo","ifconfig",interface,"hw","ether",newmac])
        subprocess.call(["sudo","ifconfig",interface,"up"])
        test.insert(END,"[+] MAC Address changed\n\n")
    else:
        test.insert(END,"\n[-] Interface Not found!\n")

def random_mac():
    interface = simpledialog.askstring(title="Interface",prompt="Choose interface to change MAC")
    check = subprocess.call(["sudo","ifconfig",interface])
    if(check == 0):
        test.insert(END,"\n[+] Changing to Random MAC...\n")
        subprocess.call(["sudo","ifconfig",interface,"down"])
        out = subprocess.check_output(["sudo","macchanger","-r",interface])
        subprocess.call(["sudo","ifconfig",interface,"up"])
        test.insert(END,out)
        test.insert(END,"\n[+] MAC Address Changed\n")
    else:
        test.insert(END,"\n[-] Interface Not found!\n")

def reset_mac():
        interface = simpledialog.askstring(title="Interface",prompt="Choose interface to change MAC")
        check = subprocess.call(["sudo","ifconfig",interface])
        if(check == 0 ):
            test.insert(END,"\n[+] Reseting Your original MAC...\n")
            subprocess.call(["sudo","ifconfig",interface,"down"])
            subprocess.call(["sudo","macchanger","-p",interface])
            subprocess.call(["sudo","ifconfig",interface,"up"])
            test.insert(END,"\n[+] Your MAC Address Reset Success")
        else:
            test.insert(END,"\n[-] Interface Not Found!\n")
#start the code--
gui = Tk()
gui.geometry("600x600")
gui.title("MACCHANGER @ PHY-Cybersec")
gui.resizable(width=False, height=False)
gui.config(bg='black')

#like string storage
#var = StringVar()
#title lable--
lable1 = Label(gui, text="MAC-CHANGER",font=("courier",40,"underline"))
lable1.pack(padx=20,pady=10)
lable1.config(bg='black',fg='white')

#Set Buttons--
btn = Button(gui,
            text="Show MAC",
            command=show_mac,
            bg='black',fg='white',activebackground='white',activeforeground='black').place(x=10,y=100)

btn = Button(gui,
            text="Show Interface",
            command=show_interface,
            bg='black',fg='white',activebackground='white',activeforeground='black').place(x=130,y=100)
btn = Button(gui,
            text="Set New MAC",
            command=manual_mac,
            bg='black',fg='white',activebackground='white',activeforeground='black').place(x=280,y=100)
btn = Button(gui,
            text="Set Random MAC",
            command=random_mac,
            bg='black',fg='white',activebackground='white',activeforeground='black').place(x=420,y=100)
btn = Button(gui,
            text="Reset MAC",
            command=reset_mac,
            bg='black',fg='white',activebackground='white',activeforeground='black').place(x=250,y=200)

socialbtn = Button(gui,
                    text="Follow Author",
                    command=follow,
                    bg='blue',fg='white',activebackground='white',activeforeground='blue').place(x=0,y=250)
#log lable--
log1 = Label(gui, text="Status:",font=("courier",20,"underline"),bg='black',fg='white').place(x=0,y=320)

#set Log details here----
test = Text(fg='green',bg='black')
test.place(x=0,y=350,height=250,width=600)

#Run GUI In loop--
gui.mainloop()
