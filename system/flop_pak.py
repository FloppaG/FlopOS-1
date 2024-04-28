import os

def install():
  app = input("App: ")
  
  if app == "snake":
    os.system("mkdir snake")
    os.system("git clone https://github.com/ading2210/snake-cli snake ")
    with open("apps.txt", "w") as file:
        file.write("snake\n")
def remove():
  app = input("App:")
  if app == "snake":
    print("Deleteing snake...")
    os.system("rm -rf snake")
    os.system("clear")