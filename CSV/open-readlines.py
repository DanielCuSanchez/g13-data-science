
with open("file-load.csv","r") as file:
  content = file.readlines()

header = content[1:2]
rows = content[3:]

print("================HEADER===========")
print(header)
print("================ROWS===========")
print(rows)