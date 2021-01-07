#!/usr/bin/python3.9

import os,sys
try:
  import requests,re
except:
  os.system('pip install requests')
  
if len(sys.argv) > 1:
  url = sys.argv[1]
  path = open(sys.argv[2],'r').read().splitlines()
  print('\n[!] PATH / FILE FOUND:')
  for page in path:
    target = url + "/" + page
    r = requests.get(target)
    if r.status_code == 200 and r.text != None:
      print('\033[32;1m'+target+'\033[00;0m')
      continue
    else:
      continue
    print('\nIt\'s done')
else:
  quit("""
[#] -------------------
[#] URL FUZZER
[#] Fuzzing paths or files exist in url
[#] Made by EtcAug10
[#] -------------------

[()] USAGE:
     python Urlfuz.py [WEB] [WORDLISTS]
[()] EXAMPLE:
     python Urlfuz.py http://d45h7.my.id pages.txt
  """)