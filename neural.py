import os
import random

def get_reply():
  alltext = open("allfiles.txt", "r").read()
  masse = alltext.split('\n')
  lengths = len(masse)
  allleng = lengths-1
  randomn = random.randint(0, allleng)
  random = masse[randomn]
  
def add_phrase(phrase):
  allsd = 'echo "'+phrase+'">>allfiles.txt'
  os.system(allsd)
  return get_reply()
