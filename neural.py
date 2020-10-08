import os
import random

def get_que(bonus):
  st = 0
  alltext = open("allfiles.txt", "r").read()
  masse = alltext.split('\n')
  questions = []
  answer = []
  lengths = len(masse)
  while (st<lengths):
    if (('?') in masse[st]):
      questions.append(masse[st])
    else:
      answer.append(masse[st])
    st +=1
  le = len(questions)
  an = len(answer)
  alleng = an-1
  allleng = le-1
  if (bonus == 'q'):
    randomn = random.randint(0, alleng)
    return (answer[randomn])
  else:
    randomn = random.randint(0, allleng)
    return (questions[randomn])

def get_ans():
  
  return a

def get_reply():
  alltext = open("allfiles.txt", "r").read()
  masse = alltext.split('\n')
  lengths = len(masse)
  allleng = lengths-1
  randomn = random.randint(0, allleng)
  return(masse[randomn])
  
def add_phrase(phrase, admin,bo):
  if (admin == True):
    allsd = 'echo "'+phrase+'">>allfiles.txt'  
    os.system(allsd)  
    return get_que(bo)
  else:
    return get_que(bo)
