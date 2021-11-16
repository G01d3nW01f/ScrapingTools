#!/usr/bin/python3

import os
import subprocess
import sys
from bs4 import BeautifulSoup as bs4
import datetime

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
    current_dir = os.getcwd() 
    if len(sys.argv) != 3:
        print(bcolors.RED,"[!]Need More Argument",bcolors.ENDC)
        usage = """
+------------------------------------------- - -- -- -- - - ---- -  --
| +------------------+   [+]Usage:                                             
| |       ___        |                                            
| |   _  (,~ |   _   |      {arg0} <target_directory_list> <keyword_list>     
| |  (____/  |____)  |                                               
| |  |||||    |||||  |   [+]Example:
| |  |||||    |||||  |      
| |  |||||\  /|||||  |      {arg0} directory_list keyword.txt 
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
        print("[+]CLEAR")
        
        if "directory" in subprocess.getoutput(f"file {sys.argv[1]}"):

            signal = "single"
            print(bcolors.GREEN,banner,bcolors.ENDC)
            return signal,current_dir
        
        else:
            signal = "list"
            print(bcolors.RED,banner,bcolors.ENDC)
            return signal,current_dir

    ##############################################################
    ## below functions are processing the list of multi target. ##
    ## took the first arguments if that are target_list,        ##
    ## then find the all list of full path.                     ##
    ## and that's list is into array and will return            ##
    ##############################################################
        
def target_list():
    
    current_dir = os.getcwd()
    targets = sys.argv[1]
    f = open(targets,"r")
    target_list = f.read().split("\n") 

    while True:
        target_list.remove("")
        if "" not in target_list:
            break

    full_path_list = []
    
    for i in target_list:
        #print(i)
        s = subprocess.getoutput(f"find {current_dir} -name {i} -type d 2> /dev/null")
        full_path_list.append(s)

    #print(full_path_list)
    return full_path_list


    ###########################################
    # the functions for the SingleTarget mode #
    # but system is similar as list attacking #
    ###########################################


def target_path():

    current_dir = os.getcwd()
    target = sys.argv[1]
    
    try: 
        full_path = subprocess.getoutput(f"find {current_dir} -name {target} -type d 2> /dev/null")
    except:
        print(bcolors.RED,f"[!]SomeExceptionOccured",bcolors.ENDC)
        sys.exit()

    full_path_list = [full_path]
    #print(full_path_list)
    return full_path_list


######################################
# For modules that some little works #
######################################

def make_directory(): 
    
    array = [" ",",","-",":"]
    test_dir = str(datetime.datetime.now())

    for i in array:
        test_dir = test_dir.replace(i,"_")
    
    os.mkdir(test_dir)
    
    abs_path = os.getcwd()+"/"+test_dir+"/"
    #print(abs_path)
     

    return abs_path



def count_keywords():

    counter = {}
    keyword_list = sys.argv[2]
    try:
        f = open(keyword_list,"r")
    except:
        print(bcolors.RED,"[!]Keyword list file is Invalid",bcolors.ENDC)
        sys.exit()
    key_words = f.read().split("\n")
     
    while True:
        key_words.remove("")
        if "" not in key_words:

            break
    
    for i in key_words:
        counter[i] = 0
       
    return key_words,counter


def aiming(full_path_list,current_dir):
    
    abs_path = make_directory()
    print(bcolors.BLUE,abs_path,bcolors.ENDC)

    for i in full_path_list:
        key_words,counter = count_keywords()   
        root_path = i.replace(current_dir,"").replace("/","")
        print(bcolors.BLUE,root_path,bcolors.ENDC)
        dirs = subprocess.getoutput(f"find {i} -type f 2> /dev/null")
        dirs = dirs.rsplit("\n")    
        f = open(abs_path+"/"+root_path,"w")

        for i in dirs:
            f2 = open(i,"r")
            
            try:
                soup = bs4(f2,"html.parser")
                for i in key_words:

                    pointer = soup.text.count(i)
                    counter[i]+=pointer
                
                for i in counter:

                    f.write(f"{i} -> {counter[i]}"+"\n")
                f.close()

            except:
                pass
                                
def main():

    signal,current_dir = init()
    
    if signal == "list":
        full_path_list = target_list()

    elif signal == "single":
        full_path_list = target_path()

    #make_directory()
    #counter()
    
    aiming(full_path_list,current_dir)

if __name__ == "__main__":

    main()
