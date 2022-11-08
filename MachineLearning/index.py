import numpy
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

file = pd.read_csv("file-load.csv")

datasetFinal = file["Final"]

mean = numpy.mean(datasetFinal)
mode = stats.mode(datasetFinal,keepdims=False)
median = numpy.median(datasetFinal)

print(mean)
print(datasetFinal.mean())

print(mode)
print(datasetFinal.mode())


print(median)
print(datasetFinal.median())


print(numpy.std(datasetFinal))
print(datasetFinal.std())

print(numpy.var(datasetFinal))
print(datasetFinal.var())


print(numpy.percentile(datasetFinal, 45))
print(datasetFinal)


#x = numpy.random.normal(5.0, 1.0, 100000)
#plt.hist(x, 100)
#plt.show()


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#Since here

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

#Until here