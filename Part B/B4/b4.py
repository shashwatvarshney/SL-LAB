from functools import reduce
import operator
f=open("myfile.txt","r")
mydict = dict()
for line in f:
    words = line.split()
    for word in words:
        if word not in mydict:
            mydict[word] = 1
        else:
            mydict[word] += 1

print(mydict)

mydict=dict(sorted(mydict.items(),key=lambda x:x[1],reverse=True))
print(mydict)
print("10 most occurences words in descending order:\n",list(mydict.keys())[:10])

lenlist=[]
for x in mydict:
    a=len(x)
    lenlist.append(a)

print(lenlist)

average=reduce(lambda x,y:x+y,mydict.values())/len(mydict.values())
print("Average length is:",average)

list2=[x for x in lenlist if (x%2!=0)]
print(list2)
def duplicate(y):
    return list(dict.fromkeys(y))

list3 = duplicate(list2)
print(list3)
list4 = [x*x for x in list3]
print(list4)
