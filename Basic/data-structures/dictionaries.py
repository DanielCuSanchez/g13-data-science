# Dictionaries: They are similar like objects in JS, the way the data is stored is with keys and values.

myCourse = {
  "name":"Datascience",
  "duration":"1 month",
  "sensei":"Daniel"
}

print(myCourse)
print(type(myCourse))

for key in myCourse.keys():
  print(key)

print("---------------------")

for value in myCourse.values():
  print(value)

print("---------------------")

for key, value in myCourse.items():
  print(key, value)

print("---------------------")