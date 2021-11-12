#!/usr/bin/python3

import os.path

from os import makedirs
import re
import sys
import subprocess


class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


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
    
    if len(sys.argv) != 2:
        print(bcolors.RED,"[!]Need More Argument!!!!!!!!!!!!!",bcolors.ENDC)
        usage = """
                        [!]Usage:
          \       /   
            .---.       {arg0} <TargetDirectory>
       '-.  |   |  .-'    
         ___|   |___    [+]First.... capture the dir and files with gdigger.py to target_site
        [           ]   [+]Step2.... this script run aim to captured 
        `---.   .---'
     __||__ |   | __||__
     '-..-' |   | '-..-'
       ||   |   |   ||
       ||_.-|   |-,_||
     .-"`   `"`'`   `"-.
   .'                   '.
"""
        usage = usage.replace("{arg0}",sys.argv[0])
        print(bcolors.BLUE,usage,bcolors.ENDC) 
        sys.exit()

    target_dir = sys.argv[1]
    
    try:
        os.chdir(target_dir)
        print(bcolors.BLUE,banner,bcolors.ENDC)
    except:
        print(bcolors.RED,"[!]SomeException Occured!!!!",bcolors.ENDC)
        sys.exit()

def get_list():
    
    all_list = subprocess.getouput("ll")
    print(all_list)



def main():

    init()
    get_list()

if __name__ == "__main__":

    main()

