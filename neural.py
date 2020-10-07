import os
import random

def get_reply():
  alltext = fopen("allfiles.txt", "w").read()
  masse = alltext.split('\n')
  lengths = len(masse)
  allleng = lengths-1
  randomn = random.randint(0, allleng)
  random = masse[randomn]
  
def add_phrase(phrase):
  alltext = fopen("allfiles.txt", "w").read()
  allsd = 'echo "'+phrase+'">>allfiles.txt'
  os.system(allsd)
  return get_reply()
