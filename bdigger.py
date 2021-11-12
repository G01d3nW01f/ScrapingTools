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

test_files = {}

banner = """
 ______   _______  _______           _______  ______  _________ _______  _______  _______  _______
(  ___ \ (  ____ )(  ___  )|\     /|(  ____ \(  __  \ \__   __/(  ____ \(  ____ \(  ____ \(  ____ )
| (   ) )| (    )|| (   ) || )   ( || (    \/| (  \  )   ) (   | (    \/| (    \/| (    \/| (    )|
| (__/ / | (____)|| (___) || |   | || (__    | |   ) |   | |   | |      | |      | (__    | (____)|
|  __ (  |     __)|  ___  |( (   ) )|  __)   | |   | |   | |   | | ____ | | ____ |  __)   |     __)
| (  \ \ | (\ (   | (   ) | \ \_/ / | (      | |   ) |   | |   | | \_  )| | \_  )| (      | (\ (
| )___) )| ) \ \__| )   ( |  \   /  | (____/\| (__/  )___) (___| (___) || (___) || (____/\| ) \ \__
|/ \___/ |/   \__/|/     \|   \_/   (_______/(______/ \_______/(_______)(_______)(_______/|/   \__/
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

    print(banner)

    usage = """

[+]Usage:
    {arg0} <Target_URL>
            or
    {arg0} <Target_List file>

[+]Example:

    {arg0} http://target_site.com/
            or
    {arg0} target_list.txt

"""

    if len(sys.argv) != 2:
        
        print("[!]NeedMoreArgument!!!!!!")
        print(usage)
        sys.exit()

    else:

        url = sys.argv[1]

        if "http" not in url:

            mode = "craster"
        
        else:
            mode = "sniper"
    
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
   return result

def download_file(url):
   o = urlparse(url)
   savepath = "./" + o.netloc + o.path
   if re.search(r"/$", savepath):
      savepath += "index.html"
   savedir = os.path.dirname(savepath)

   if os.path.exists(savepath): return savepath

   if not os.path.exists(savedir):
      print("mkdir=", savedir)
      makedirs(savedir)

   try:
      print("download=", url)
      urlretrieve(url, savepath)
      time.sleep(1)
      return savepath
   except:
       print("[!]Download Failed:", url)
       return None

def analize_html(url, root_url):
   savepath = download_file(url)
   if savepath is None: return
   if savepath in test_files: return
   test_files[savepath] = True
   print("analize_html=", url)
   

   html = open(savepath, "r", encoding="utf-8").read()
   #html = open(savepath, "r", encoding="CP932").read()
   #html = open(savepath, "r", encoding="Shift_JIS").read()
   #html = open(savepath, "r", encoding="EUC-JIS").read()

   links = enum_links(html, url)
   for link_url in links:
      if link_url.find(root_url) != 0:
         if not re.search(r".css$", link_url): continue

      if re.search(r".(html|htm)$", link_url):
         analize_html(link_url, root_url)
         continue

      download_file(link_url)

def main():

    url,mode = init()
    analize_html(url,url)


if __name__ == "__main__":
   main()
