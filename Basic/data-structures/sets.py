# Sets: They are unordered, unchangeable, unindexed and they can not accept duplicated values. It is case sensitive.

myList = ["Jonathan", "Rikson", "Hugo", "Hugo", "Betsy", "betsy", "betsy"]

mySet = set(myList)

print(mySet)
print(type(mySet))

myList = list(mySet)
print(myList)

