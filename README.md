
#   I thought 
  scrape the web site and clone it
  after the analysis the html for link and scripts or information from CMS and versions and more....
    
   So I thought web_page clone or copy and these into directory_file that is not bad idea...
    
```
                    +---------------+
<Target WebSite>    |WebSite <clone>|                            ------------------------
                    +---------------+              +-----+       |      Anlysis  
                            |              +-------|Page1|-----<html>   Search
                      +-----------+        |       +-----+       |      Compare
                      |directory 1|--------+                     |      ExtractLink
                      +-----------+        |       +-----+       |      ......
                            |              +-------|Page2|-----<html>
                            |                      +-----+       |
                            |                      +-----+       |
                            |              +-------|Page1|-----<html>
                      +-----------+        |       +-----+       |
                      |directory 2|--------+                     |
                      +-----------+        |       +-----+       |
                                           +-------|Page2|-----<html>
                                                   +-----+       |------------------------

```                                                               


# GraveDigger
  scraping and crawling tool.
  download the target site's html to local,
  and make folder in depending on the depth with crawl
  
  however this script is not useful!!!!!!!!!!
  
  
 ```
 $ ./gdigger.py https://webscraper.io/test-sites/                 
 
 ____  _____  ___  __ __ _____ _____ __  ____   ____  _____ _____
(( ___ ||_// ||=|| \\ // ||==  ||  ) || (( ___ (( ___ ||==  ||_//
 \\_|| || \\ || ||  \V/  ||___ ||_// ||  \\_||  \\_|| ||___ || \
 ____,
/.---|
`    |     ___      __________
    (=\.  /-. \`   |          |
     |\/\_|"|  |  <  hello ?? | 
     |_\ |;-|  ;   |__________|
     | / \| |_/ \`
     | )/\/      \`
     | ( '|  \   |
     |    \_ /   \
     |    /  \_.--\
     \    |    (|\`
      |   |     \
      |   |      '.
      |  /         \
      \  \.__.__.-._)
 
 [+]Mode: Sniper 
 [+]download =>  https://webscraper.io/test-sites/ 
 [>>]analize_html => https://webscraper.io/test-sites/ 
 [+]download =>  https://webscraper.io/test-sites/e-commerce/allinone 
 [+]download =>  https://webscraper.io/test-sites/e-commerce/static 
 [+]download =>  https://webscraper.io/test-sites/e-commerce/allinone-popup-links 
 [+]download =>  https://webscraper.io/test-sites/e-commerce/ajax 
 [+]download =>  https://webscraper.io/test-sites/e-commerce/more 
 [+]download =>  https://webscraper.io/test-sites/tables 
 
 ```
  Sniper mode is one target only
  But if you have list of targets, put the list_file on arguments
  
  then this script will do in craster mode
  
 ```
 killskill-picoctf@webshell:~/dev/grave_digger$ ./gdigger.py list.txt
 
 ____  _____  ___  __ __ _____ _____ __  ____   ____  _____ _____
(( ___ ||_// ||=|| \\ // ||==  ||  ) || (( ___ (( ___ ||==  ||_//
 \\_|| || \\ || ||  \V/  ||___ ||_// ||  \\_||  \\_|| ||___ || \
 ____,
/.---|
`    |     ___      __________
    (=\.  /-. \`   |          |
     |\/\_|"|  |  <  hello ?? | 
     |_\ |;-|  ;   |__________|
     | / \| |_/ \`
     | )/\/      \`
     | ( '|  \   |
     |    \_ /   \
     |    /  \_.--\
     \    |    (|\`
      |   |     \
      |   |      '.
      |  /         \
      \  \.__.__.-._)
 
 [+]Mode: Craster 
 [+]MakeDirectory =>  ./checkip.dyndns.org 
 [+]download =>  http://checkip.dyndns.org/ 
 [>>]analize_html => http://checkip.dyndns.org/ 
 [+]MakeDirectory =>  ./toscrape.com 
 [+]download =>  http://toscrape.com/ 
 [>>]analize_html => http://toscrape.com/ 
 [+]MakeDirectory =>  ./toscrape.com/css 
 [+]download =>  http://toscrape.com/css/bootstrap.min.css 
 [+]download =>  http://toscrape.com/css/main.css 
 
 ```
 
 
 
 # Catacumba
 
 catacumba is keyword searching tools for after the gravedigger clone files.
 
 ```
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
                      
```

This Script is wrote for generated clone file for targetting web sites.
but if you can make more better clone than grave digger, then please tell me, and give me, 
ofcourse I will use it.

by the way, any this tool find the keywords in every page and text,



# Huckebein

```
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
 ```
 Huckebein is are email_address find tool, ofcourse this tool too for downloaded clone file of targetted web site.
 information gathering is fun? oh my god, you gotta be a NSA agents.
 
 and this tool can detection to phone number but japanese only, why?? I don't know about the phone number rules of all over the fucking world
 




 
