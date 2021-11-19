#!/usr/bin/python3

import os
import subprocess
import sys
from bs4 import BeautifulSoup as bs4
import datetime
import re

class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    WHITE = '\033[37m'

banner = """
                                       /T /I
                              / |/ | .-~/  /
                          T\ Y  I  |/  /  _
         /T               | \I  |  I  Y.-~/
        I l   /I       T\ |  |  l  |  T  /
 __  | \l   \l  \I l __l  l   \   `  _. |
 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |
  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
 >--.  ~-.   ._  ~>-"    "\\   7   7   ]
^.___~"--._    ~-{  .-~ .  `\ Y . /    |
 <__ ~"-.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l______
       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.
              (_/ .  ~(   /'     "~"--,Y   -=b-. _)
               (_/ .  \  :           / l      c"~o \\
                \ /    `.    .     .^   \_.-~"~--.  )
                 (_/ .   `  /     /       !       )/
                  / / _.   '.   .':      /        '
                  ~(_/ .   /    _  `  .-<_
                    /_/ . ' .-~" `.  / \  \          ,z=.
                    ~( /   '  :   | K   "-.~-.______//
                      "-,.    l   I/ \_    __{--->._(==.
                       //(     \  <    ~"~"     //
                      /' /\     \  \     ,v=.  ((
                    .^. / /\     "  }__ //===-  `
                   / / ' '  "-.,__ {---(==-
                 .^ '       :  T  ~"   ll       
                / .  .  . : | :!        \\\\
               (_/  /   | | j-"          ~^   
  /  // /  //     /     /      /  /      /     /  /     / ////   //  / /
 _     _ _     _ _______ _     _ _______ ______  _______ _____ __   _  ,
 |_____| |     | |       |____/  |______ |_____] |______   |   | \  |
 |     | |_____| |_____  |    \_ |______ |_____] |______ __|__ |  \_|/  ,    
                    
 //..._././/..//./ .//.. .. . /// ./../../// // /../.. . /..../ ../ /.
"""

def init():
    #current_dir = os.getcwd() 
    if len(sys.argv) != 2:
        print(bcolors.RED,"[!]Need More Argument",bcolors.ENDC)
        usage = """
+------------------------------------------- - -- -- -- - - ---- -  --
| +------------------+   [+]Usage:                                             
| |       ___        |                                            
| |   _  (,~ |   _   |      {arg0} <target_directory_name(cloned)>    
| |  (____/  |____)  |                                               
| |  |||||    |||||  |   [+]Example:
| |  |||||    |||||  |      
| |  |||||\  /|||||  |      {arg0} target.com.cloned
| |  |||'//\/\\\`|||  |                                               
| |  |' m' /\ `m `|  |                                               
| |       /||\       |                                               
|  \_              _/                                                
|    `------------'       
+-------------------------------------------- --- -- -- ---- --  -- --
"""
        usage = usage.replace("{arg0}",sys.argv[0])
        print(bcolors.GREEN,usage,bcolors.ENDC)
        sys.exit()

    else:
        print(bcolors.BLUE,"[+]CLEAR",bcolors.ENDC)
        
        if "directory" in subprocess.getoutput(f"file {sys.argv[1]}"):

            signal = "single"
            print(bcolors.GREEN,banner,bcolors.ENDC)
            target = sys.argv[1]
            return signal,target
        
        else:
            signal = "list"
            print(bcolors.RED,banner,bcolors.ENDC)
            target = sys.argv[1]
            return signal,target

def into_the_arena(target):
    
    dir_path = os.getcwd()+"/"+target
    all_file_list = subprocess.getoutput(f"find {dir_path} -type f 2> /dev/null")
    all_file_list = all_file_list.rsplit("\n")
    while True:
        try:
            all_file_list.remove("")
            if "" not in all_file_list:
                break
        except:
            break

    email_address_list = []
    phone_or_fax_list  = []
    print(bcolors.GREEN,f"[+]Target: {target}",bcolors.ENDC)
    
    for i in all_file_list:

        f = open(i,"r",encoding="utf8",errors="ignore")
        soup = bs4(f,"html.parser")
        
        reg = re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",soup.text)
        if reg != None:
            email_address_list.append(reg.group())      
            print(bcolors.BLUE,f"{i} -->"+bcolors.GREEN,f"Detected email_address:{bcolors.WHITE}[{reg.group()}]",bcolors.ENDC)
    
        else:
            print(bcolors.RED,f"{i} --> NotDetected...",bcolors.ENDC)

        reg = re.search(r"\b\d{2,4}[-]\d{2,4}[-]\d{2,4}",soup.text)
        if reg != None:
            phone_or_fax_list.append(reg.group())
            print(bcolors.BLUE,f"{i} -->"+bcolors.GREEN,f"Detected phone_or_fax number:{bcolors.WHITE}[{reg.group()}]",bcolors.ENDC)
        
        else:
            print(bcolors.RED,f"{i} --> NotDetected...",bcolors.ENDC)


    email_address_list =  set(email_address_list)
    email_address_list = list(email_address_list)
    phone_or_fax_list  =  set(phone_or_fax_list)
    phone_or_fax_list  = list(phone_or_fax_list)
   
    

    empty_ascii_art = """
  _______  ___      ___    _______  ___________  ___  ___  
 /"     "||"  \    /"  |  |   __ "\("     _   ")|"  \/"  | 
(: ______) \   \  //   |  (. |__) :))__/  \\\__/  \   \  /  
 \/    |   /\\\  \/.    |  |:  ____/     \\\_ /     \\\  \/   
 // ___)_ |: \.        |  (|  /        |.  |      /   /    
(:      "||.  \    /:  | /|__/ \       \:  |     /   /     
 \_______)|___|\__/|___|(_______)       \__|    |___/      
                                                           
    """
    if len(email_address_list) == 0 and len(phone_or_fax_list) == 0:
        print(bcolors.RED,"[!]Not Detected, or Target has been there...",bcolors.ENDC)
        print(bcolors.RED,f"{empty_ascii_art}",bcolors.ENDC)
    else:
        print(email_address_list)
        print(phone_or_fax_list)

    finalize_dir_name = report_manager(target)
   
    os.system(f"touch {finalize_dir_name}_email_phone_FAX")
    print(f"[+]make_the_file!")
    f = open(finalize_dir_name+"_email_phone_FAX","w")
    
    for i in email_address_list:
        f.write("email : "+i+"\n")
    for i in phone_or_fax_list:
        f.write("number: "+i+"\n")

    f.close()

    print(bcolors.GREEN,"[+]Report Logging Done >>"+bcolors.BLUE,f"{finalize_dir_name}_email_phone_FAX",bcolors.ENDC)

def targets_to_target(target):
    
    f = open(target,"r")
    target_list = f.read().rsplit("\n")
    while True:
        try:
            target_list.remove("")
            if "" not in target_list:
                break
        except:
            break

    return target_list

def report_manager(target):
    
    reg = re.search(r".+/$",target)
    if reg != None:
        target = target[:-1]

    dir_name = "report_mail_and_phone_"+str(datetime.datetime.now()).replace(" ","").replace(":","").replace(".","")[9:]
    os.mkdir(dir_name)
    finalize_dir_name = dir_name+"/"+target+"_report"
    #print(finalize_dir_name)

    return finalize_dir_name

def main():
    signal,target = init()
    
    if signal == "single":
        into_the_arena(target)
    
    elif signal == "list":
        target_list =  targets_to_target(target)
        for i in target_list:
            into_the_arena(i)

if __name__ == "__main__":
    main()

