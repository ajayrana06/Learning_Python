#Create a variable inside a function with same name as global variable
x="awensome"
def myFunc():
    x="Fantastic"
    print("Python is",x)
myFunc()
print("Python is",x)
