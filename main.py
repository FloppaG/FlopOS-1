import os
import sys
import time
import system.flop_pak
import system.notes
import json
from random import randrange
sys.path.append('system') 
os.system('clear')

print("loading default variable values")
loadingtime = 1

prompt = "User@FlopOS "
promptold = "@FlopOS "
loginstatus = False
diskfiles = "main"
filescount = 0
run = 2
bypass_code = os.environ['bypass_code']

def sysexit(val):
  if val == False: 
    print("FlopOS-checker: all right")
  elif val == True:
    sys.exit()
    insideval = True
  elif val == "onstart":
    print("FlopOS-checker is running.")
  elif insideval == True:
    sys.exit()

os.system('clear')

print("Running FlopOS-checker.")
sysexit("onstart")

print("creating memory variables")
memory1 = 0
memory2 = 0
memory3 = 0
memory4 = 0
memory5 = 0
memory6 = 0
memory8 = 0
memory9 = 0
memory10 = 0
memory11 = 0
memory12 = 0
memoryfull = False
os.system('clear')

print("loading default lists")
os.system('clear')
position = ["files", "games", "system"]
main = ["files", "games", "system"]
disk = ["main"]
files = {"README.txt": "ADD HERE A TEXT" , "New file.txt": ""}

print("loading deatful definitoins")
os.system('clear')
def GetDirByPosition(pos):
  print(pos)

def checkMemory():
  if memory1 != 0 and memory12 != 0 and memory5 != 0:
    memoryfull = True
  else:
    memoryfull = False

def native_cmd(input):
  print("This is your native command line. enter flopos to go back to the flopOS.")
  time.sleep(3)
  if input == "flopos":
     sys.exit()
  else:
    os.system(input)

print("Starting")
time.sleep(loadingtime)
Check = False

with open('system/daily.json') as f:
  data = json.load(f)

category_data = data['daily']
number = randrange(1, 5)
number = str(number)

result = category_data[number]

print('FlopOS 1.2\nRandom FlopOS Fact:' + result)

while 1 < run:
  checkMemory()
  cmd = input(prompt)
  if cmd == "help":
    print("help - show all commands.")
    print("cls - clear screen.")
    print("prompt - set custom prompt.")
    print("prompt.deatful - set prompt to deatful.")
    print("prompt.old - set prompt to prompt, which you used before.")
    print("ls show folders.")
    print("version - show version.")
    print("note create - creates a note.")
    print("note edit - edits a note.")
  elif cmd == "flop-pak install":
    system.flop_pak.install()

  elif cmd == "flop-pak remove":
    system.flop_pak.remove()
  elif cmd == "cd":
    input("Dir ")
    if input == "files":
      position = "files";
    elif input == "games":
      print("Coming soon!!")
    elif input == "system":
      position = "system"
    else:
      print("Can't find a folder.\nThere can be a bug in code, please contact us if found.")
  elif cmd == "report":
    print("Coming soon!!")
  elif cmd == "cls":
    os.system('clear')
    print("FLOP-OS")
  elif cmd == "prompt":
    promptold = prompt
    prompt = input("Custom prompt: ")
  elif cmd == "prompt.deatful":
    prompt = "User@FlopOS  "
  elif cmd == "prompt.old":
    prompt = promptold
  elif cmd == "version":
    print("This is FlopOS 1! The first version of the FlopOS operating system. Last upda"+"te date: 04.27.2024")
#  elif cmd == "dev panel":
#    if role
  elif cmd == "ls":
    GetDirByPosition(position)
  elif cmd == "mkfile":
    filescount = filescount + 1
    filename = "file" + " " + str(filescount)
    content = input("content: ")
    files[filename] = content
  elif cmd == "native_cmd":
    native = input("native_cmd: ")
    native_cmd(native)
  elif cmd == "note create":
    path = input("name/path: ")
    text = input("text: ")
    system.notes.create(path, text)
  elif cmd == "note edit":
    path = input("path: ")
    system.notes.edit(path)
  elif memoryfull == True:
    print("system overloaded")
    sys.exit()
  elif cmd == "shutdown":
    sys.exit()
