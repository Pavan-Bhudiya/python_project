import module
# inbuilt of import of math,statistics,date&time
import math
import statistics
import datetime

module.hello("Erick")
module.hello("Daniel")

# import of inbuilt math
print(math.sqrt(64))
print(math.e)

# mean using import of statistics
dataset=[3,5,9,6,8,7]
x=statistics.mean(dataset)
y=statistics.median(dataset)
z=statistics.mode(dataset)
f=statistics.fmean(dataset)
r=statistics.quantiles(dataset)
e=statistics.variance(dataset)
print("The Mean is ", x)
print("The Median is ",y)
print("The Mode is ",z)
print("The Fmean is ",f)
print("The Quartiles is ",r)
print("The Variance is ",e)
# import of date&time now
masaa=datetime.datetime.now()
print(masaa)

# importing of a module
import module
module.org("Kaspersky")


