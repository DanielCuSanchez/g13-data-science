

subtraction = lambda n1, n2 : n1 - n2

#print(subtraction(5,3))


# function base
#functionExample = lambda input, baseNumber : input * baseNumber
def myBaseFunction(baseNumber):
  return lambda input : input * baseNumber

function3 = myBaseFunction(3)
function10 = myBaseFunction(10)
function5 = myBaseFunction(5)

for i in range(10):
  print(function10(i + 1))
