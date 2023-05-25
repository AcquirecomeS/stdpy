def mycalc(n):
    return abs(n - 3)

num = [1,2,3,4,5,6,7,8,9]
num.sort(key = mycalc)
print(num)
num.append("10")
print(num)
num.insert(0,"0")
print(num)
num.remove("10")
print(num)
num.reverse()

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
mylist=thislist+num
print(mylist)
newnum=num.copy()
num.clear()
print(newnum)
del num