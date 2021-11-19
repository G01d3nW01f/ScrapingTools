#!/usr/bin/python3

from bs4 import BeautifulSoup
import urllib
import urllib.request
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.request import urlretrieve
from os import makedirs
import os.path
import time
import re
import sys

class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

test_files = {}

banner = """
 ____  _____  ___  __ __ _____ _____ __  ____   ____  _____ _____
(( ___ ||_// ||=|| \\\ // ||==  ||  ) || (( ___ (( ___ ||==  ||_//
 \\\_|| || \\\ || ||  \V/  ||___ ||_// ||  \\\_||  \\\_|| ||___ || \\\
 ____,
/.---|
`    |     ___      __________
    (=\.  /-. \`   |          |
     |\/\_|"|  |  <  hello ?? | 
     |_\ |;-|  ;   |__________|
     | / \| |_/ \`
     | )/\/      \`
     | ( '|  \   |
     |    \_ /   \\
     |    /  \_.--\\
     \    |    (|\`
      |   |     \\
      |   |      '.
      |  /         \\
      \  \.__.__.-._)
"""


def init():
    
    usage = """
----------------------------------------------------------
         +-----+        [+]Usage: 
         |     |            {arg0} <Target_URL>
   +-----+     +-----+            or
   |                 |      {arg0} <Target_List File>
   +-----+     +-----+
         |     |        [+]Example:
         |     |            {arg0} http://target_site.com/
         |     |                  or
         |     |            {arg0} target_list.txt
---------+     +-------------------------------------------
"""
    usage = usage.replace("{arg0}",sys.argv[0])

    if len(sys.argv) != 2:
        
        print(bcolors.RED,"[!]NeedMoreArgument!!!!!!")
        print(usage,bcolors.ENDC)
        sys.exit()

    else:
        print(bcolors.GREEN,banner,bcolors.ENDC)
        url = sys.argv[1]
        reg = re.search(r"(http.+)",url)

        if reg != None: 
            mode = "sniper"
        else: 
            mode = "craster"
       
        reg = re.search(r"[/]$",url)
        if reg == None:
            url = url+"/"
        print(url)

    del usage,reg
    return url,mode

def enum_links(html, base):
   soup = BeautifulSoup(html, "html.parser")
   links = soup.select("link[rel='stylesheet']")
   links += soup.select("a[href]")
   result = []

   for a in links:
      href = a.attrs['href']
      url = urljoin(base, href)
      result.append(url)
   
   #del soup,links,href,url

   return result





def download_file(url):
   o = urlparse(url)
   savepath = "./" + o.netloc + o.path
   if re.search(r"/$", savepath):
      savepath += "index.html"
   savedir = os.path.dirname(savepath)

   if os.path.exists(savepath): return savepath

   if not os.path.exists(savedir):
      print(bcolors.BLUE,"[+]MakeDirectory => ", savedir,bcolors.ENDC)
      makedirs(savedir)

   try:
      print(bcolors.YELLOW,"[+]download => ", url,bcolors.ENDC)
      urlretrieve(url, savepath)
      time.sleep(1)
      return savepath
   except:
       print(bcolors.RED,"[!]Download Failed:", url,bcolors.ENDC)
       return None

    
    
    
def analize_html(url, root_url):
   savepath = download_file(url)
   if savepath is None: return
   if savepath in test_files: return
   test_files[savepath] = True
   print(bcolors.GREEN,"[>>]analize_html =>", url,bcolors.ENDC)

   try:
       html = open(savepath, "r", encoding="utf-8").read()

   except:

       html = open(savepath, "r", encoding="CP932").read()
   
   #except:
   #    html = open(savepath, "r", encoding="Shift_JIS").read()
   
   #except:
   #    html = open(savepath, "r", encoding="EUC-JIS").read()

   links = enum_links(html, url)
   for link_url in links:
      if link_url.find(root_url) != 0:
         if not re.search(r".css$", link_url): continue

      if re.search(r".(html|htm)$", link_url):
         analize_html(link_url, root_url)
         continue

      download_file(link_url)

    #del savepath,html

    
    
def claster_bomb(url):

    target_list = url
    
    try:
        f = open(target_list,"r")
    except:
        print(bcolors.RED,"[!]Some Exception Occured",bcolors.ENDC)
        sys.exit()

    for i in f:
        analize_html(i.rstrip("\n"),i.rstrip("\n"))

        
        
def mode_selector(url,mode):

    if mode == "sniper": 
        print(bcolors.RED,"[+]Mode: Sniper",bcolors.ENDC)
        analize_html(url,url)
    
    else:
        print(bcolors.RED,"[+]Mode: Craster",bcolors.ENDC)
        claster_bomb(url)

     
def main():

    url,mode = init()
    mode_selector(url,mode)
    
if __name__ == "__main__":
   main()

