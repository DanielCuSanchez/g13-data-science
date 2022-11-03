import csv

rows = []

with open("file-load.csv","r") as file:
  reader = csv.reader(file) #[[]['Last_name', ' "First name"']["a1","n1"]["a1","n1"]["a1","n1"]]
  empty = next(reader)
  for row in reader:
    rows.append(row)

header = rows[0] # [['Last_name', ' "First name"']]["a1","n1"][][]]
print(empty)
print("===================================================")
print(header)
print("===================================================")
print(rows[1:])