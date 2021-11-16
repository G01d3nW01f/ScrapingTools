#!/usr/bin/python3

import os.path
from os import makedirs
import re
import sys
import subprocess
from bs4 import BeautifulSoup as bs4

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
        [           ]   [+]Step2.... this script run aim to captured 
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

    while True:
        keyword_list.remove("")
            
        if "" not in keyword_list:
            break
    
    list_attack_flag = subprocess.getoutput(f"file {target_dir}")
    
    absolute_path = os.getcwd()
    #os.chdir(target_dir)
    print(bcolors.BLUE,banner,bcolors.ENDC)
    
    if "directory" not in list_attack_flag:
        print(bcolors.RED,"[*]List_Attack",bcolors.ENDC)
        signal = "List"

    else:
        print(bcolors.RED,"[*]Single_Attack",bcolors.ENDC)
        signal = "Single"
        os.chdir(target_dir)

    return absolute_path,keyword_list,signal
    
   
def get_list(absolute_path):
    
    current_directory = os.getcwd()

    all_dir = subprocess.getoutput(f"find {current_directory} -type d 2> /dev/null")
    all_dir = all_dir.rsplit("\n")

    #print(bcolors.GREEN,"[+]All_Directory....",bcolors.ENDC)
    
    for i in all_dir:
        i = i.replace(absolute_path,"")
        #print(bcolors.BLUE,i,bcolors.ENDC)
    
    del all_dir,i 
    return current_directory


def file_path(current_directory,absolute_path):

    all_file = subprocess.getoutput(f"find {current_directory} -type f 2> /dev/null")
    all_file = all_file.rsplit("\n")

    print(bcolors.GREEN,"[+]founded_file:",bcolors.ENDC)
    
    for i in all_file:
        i = i.replace(absolute_path,"")
        print(bcolors.BLUE,i,bcolors.ENDC)

    return all_file

def counter(all_file,keyword_list):
    
    dic = {}
    print(bcolors.GREEN,"[+]KeyWordList: ",bcolors.ENDC)
    print(bcolors.YELLOW,keyword_list,bcolors.ENDC)
    for i in keyword_list:
        dic[i] = 0
    
    #print(dic)

    for i in all_file:
        
        f = open(i,"r")

        try:
            soup = bs4(f,"html.parser")
            #print(soup.text)
            
            for i in keyword_list:
                
                pointer = soup.text.count(i)
                dic[i]+=pointer
    
        except:
            pass
    
    for i in keyword_list:
        
        if dic[i] == 0:
            print(bcolors.RED,f"{i} --> {dic[i]}",bcolors.ENDC)
        
        elif dic[i] > 9:
            print(bcolors.WHITE,f"{i} --> {dic[i]}",bcolors.ENDC)

        else:
            print(bcolors.BLUE,f"{i} --> {dic[i]}",bcolors.ENDC)
        
    return keyword_list,dic

def report_manager(absolute_path,current_directory):

    file_dir = current_directory.replace(absolute_path,"")
    file_dir = file_dir.replace("/","report.")
    
    print(bcolors.YELLOW,f"Write to: {file_dir}",bcolors.ENDC)
    print(bcolors.YELLOW,f"FullPath: {current_directory}"+"/"+f"{file_dir}",bcolors.ENDC)

    return file_dir

def processing(keyword_list,dic,file_dir):

    f = open(file_dir,"w")
    f.write(file_dir.replace("report.","")+"\n")
    for i in keyword_list:

        f.write(i+","+str(dic[i])+"\n")

    f.close()
    #os.system(f"cat {file_dir}")

def list_cutter(keyword_list):
    
    target_list = sys.argv[1]
    f = open(target_list,"r")
    target_list = f.read().split("\n")
    while True:
        target_list.remove("")
        if "" not in target_list:
            break
    current_dir = os.getcwd()
    for i in target_list:

        specify_dir_name = subprocess.getoutput(f"find {current_dir} -type d -name {i} 2>/dev/null")
        print(specify_dir_name)
    

    



def main():

    absolute_path,keyword_list,signal = init()
    
    if signal == "Single":

        current_directory = get_list(absolute_path)
        all_file = file_path(current_directory,absolute_path)
        keyword_list,dic = counter(all_file,keyword_list)
        file_dir = report_manager(absolute_path,current_directory)
        processing(keyword_list,dic,file_dir)

    else:

        list_cutter(keyword_list)
        
        

#######################################################
# MainFunction is not write for some implementation   #
# why? beacuse I can not management god damn function #  
#######################################################

if __name__ == "__main__":

    main()
