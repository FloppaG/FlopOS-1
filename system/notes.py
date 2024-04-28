def edit(path):
  contents = open(path, "r").read()
  text = input(contents)
  with open(path, "w") as file:
    file.write(contents+text)
def create(path, text):
  with open(path, "w") as file:
    file.write(text)