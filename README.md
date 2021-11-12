# GraveDigger
  scraping and crawling tool.
  download the target site's html to local,
  and make folder in depending on the depth with crawl
  
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
 
 
 
 
 
