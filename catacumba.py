#!/usr/bin/python3

import os.path
from os import makedirs
import re
import sys
import subprocess
from bs4 import BeautifulSoup as bs4
import datetime
import logging


class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    WHITE = '\033[37m'

banner = """
 _______ _______ _______ _______ _______ _     _ _______ ______  _______
 |       |_____|    |    |_____| |       |     | |  |  | |_____] |_____|
 |_____  |     |    |    |     | |_____  |_____| |  |  | |_____] |     |
                    
                     Mors stupebit et natura,
                   _.----------------------------._
               _.-'          '-        .           '-._
             .'      _|   .    . - .        ._         '.
          _.'    '           .'     '.               _| |
         /  _|        _|    ''       ''  |_     '    .  '.
        |      . -- .      ''         ''      . -- .     |
       .'    .'      '.   -||         ||    .'      '.   '.
       | '  ''        ''   ||   .-.   ||_  ''        ''   |
       '.  ''          ''  ||   | |   ||  ''          ''  |
        | -||          ||- '____|!|____' -||          ||- |
        |  ||          ||  |____-+-____|  ||          ||  '.
       .' -||          ||_ ||   |!|   ||  ||          ||  _|
       |_.-||          ||  ||   | |   || _||          ||-._|
    _.-' |_||          ||  ||   | |   ||  ||          ||_| '-._
    _| |_  |:;;.,::;,.';|--|:;;.| |,.';|--|:;;.,::;,.';|     |_
             :;;.,::;,.';   :;;.| |,.';    :;;.,::;,.';  _|   -'
       |_                       | |                         |_.
     _      _|                __|_|__              |_     _
    |________________________/_______\___________________|______
    ,:.,:.,:.,:.,:.,:.,:.,:.,:.,:.,:.,:.,:.,:.,:.,:.,:.,:.,:.,:.
    ------------------------------------------------------------
                      Cum resurget creatura
"""

def init():
    
    if len(sys.argv) != 3:
        print(bcolors.RED,"[!]Need More Argument!!!!!!!!!!!!!",bcolors.ENDC)
        usage = """
                        [!]Usage:
          \       /   
            .---.       {arg0} <TargetDirectory> <KeyWordList>
       '-.  |   |  .-'    
         ___|   |___    [+]First.... capture the dir and files with gdigger.py to target_site
        [           ]   [+]Step2.... this script run aim to captured into directory
        `---.   .---'   
     __||__ |   | __||__[!]Example:
     '-..-' |   | '-..-'
       ||   |   |   ||  {arg0} target.directory cmsdefault.txt
       ||_.-|   |-,_||
     .-"`   `"`'`   `"-.
   .'                   '.
"""
        usage = usage.replace("{arg0}",sys.argv[0])
        print(bcolors.BLUE,usage,bcolors.ENDC) 
        sys.exit()

    target_dir = sys.argv[1]
    keyword_list = sys.argv[2]
    
    try:

        f = open(keyword_list,"r")
        keyword_list = f.read().split('\n')
        
    except:

        print(bcolors,"[!]Some Exception Occured!!!!",bcolors.ENDC)
        sys.exit()
    
    list_attack_flag = subprocess.getoutput(f"file {target_dir}")
    
    absolute_path = os.getcwd()
    
    if "directory" not in list_attack_flag:
        print(bcolors.RED,"[*]List_Attack",bcolors.ENDC)
        signal = "List"
        print(bcolors.GREEN,banner,bcolors.ENDC)
    else:
        print(bcolors.RED,"[*]Single_Attack",bcolors.ENDC)
        signal = "Single"
        print(bcolors.GREEN,banner,bcolors.ENDC)
       
    return signal
#######################################
# This Function is For Only Debugging #
#######################################

def dbg():
    print(bcolors.RED,"[!]DBG!!!!!!!!!!!!!")
    print(bcolors.RED,"->",inspect.currentframe().f_lineno,bcolors.ENDC)



def args_take_off():

    targets = sys.argv[1]
    keyword = sys.argv[2]

    reg = re.search(r".+/$",targets)
    if reg != None:
        targets = targets[:-1]

    return targets,keyword



def make_directory():

    new_dir = str(datetime.datetime.now()).replace(" ","").replace("-","").replace(":","").replace(".","")[:14]
    
    try:
        os.system(f"mkdir {new_dir}")
    except:
        print(bcolors.RED,"[+]AlreadyExitsts",bcolors.ENDC)
        pass

    full_path_of_new_directory = os.getcwd()+"/"+new_dir+"/"
    print(bcolors.BLUE,"[+]NewDirectoryCreated For Report",bcolors.ENDC)
    print(bcolors.YELLOW,full_path_of_new_directory,bcolors.ENDC)
    
    return full_path_of_new_directory


def dir_recon(targets,keywords,full_path_of_new_directory):
     
    curr_dir = os.getcwd()    
    target_full_path = subprocess.getoutput(f"find {curr_dir} -name {targets} -type d 2> /dev/null")
    print(bcolors.GREEN,f"[>]FullPathOfTarget: {target_full_path}",bcolors.ENDC)
    
    target_file_full_path = subprocess.getoutput(f"find {target_full_path} -type f 2> /dev/null")
    #print(bcolors.BLUE,f"{target_file_full_path}",bcolors.ENDC)
    
    target_file_full_path = target_file_full_path.rsplit("\n") 
    while True:
        try:
            target_file_full_path.remove("")
            if "" not in target_file_full_path:
                break
        except:
            break

    print(bcolors.RED,"[>]AllTargetFiles ",bcolors.ENDC)
    for i in target_file_full_path:
        print(bcolors.WHITE,i,bcolors.ENDC)
   
    f = open(keywords,"r")
    keywords_list = f.read().rsplit("\n")

    while True:
        try:
            keywords_list.remove("")
            if "" not in keywords_list:
                break
        except:
            break

    #target_file_full_path => array of the file and not a directory for crawling
    #keywors_list => array of the keyword for searching

    dictio = {}

    for i in keywords_list:
        dictio[i] = 0

    for i in target_file_full_path:
        
        try:
            f = open(i,"r")
            soup = bs4(f,"html.parser")
            for i in keywords_list:
                pointer = soup.text.count(i)
                dictio[i]+=pointer
        except:
            pass

    #print(dictio)
    
    dir_name = full_path_of_new_directory+targets
    
    #print(dir_name)

    report_f = open(dir_name,"w")

    for i in dictio:
        report_f.write(str(i)+","+str(dictio[i])+"\n")
        
        if dictio[i] == 0:
            print(bcolors.RED,f"{i} --> {dictio[i]}",bcolors.ENDC)
        elif dictio[i] > 9:
            print(bcolors.BLUE,f"{i} --> {dictio[i]}",bcolors.ENDC)
        else:
            print(bcolors.GREEN,f"{i} --> {dictio[i]}",bcolors.ENDC)
    
    report_f.close()


def target_to_targets(targets):


    checker = subprocess.getoutput(f"file {targets}")
    if "directory" not in checker:
        print("clear")
    
    f = open(targets,"r")
    targets = f.read().rsplit("\n")
    
    
    while True:
        try:
            targets.remove("")
            if "" not in targets:
                break
        except:
            break

    return targets 

def list_attacking():
    
    targets,keyword = args_take_off()
    full_path_of_new_directory = make_directory()
    target_array = target_to_targets(targets)
    #print(target_array)
    
    for i in target_array:
        
        dir_recon(i,keyword,full_path_of_new_directory)
    
     
def single_attacking():

    targets,keyword = args_take_off()
    full_path_of_new_directory = make_directory()
    dir_recon(targets,keyword,full_path_of_new_directory)

def main():
    signal = init()
     
    if signal == "List":
        list_attacking()

    elif signal == "Single":        
        single_attacking()
   
if __name__ == "__main__":

    main()

