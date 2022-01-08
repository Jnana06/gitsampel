import functools
import math
import operator
def fun1(n,s):
    b=[]
    a=[]
    for i in range(n-1):
        a.append([s[i]])
        for j in range(i+1,n):
            a.append([s[i],s[j]])
    a.append([s[-1]])
    #a=[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
    print(a)
    for i in a:
        b.append( str(functools.reduce(operator.mul, i)))
    print(b)
    count=0
    p=[1,2,3,5,7]
    for i in b:
        if(int(i) in p):
            count=count+1
            print("yes")
        else:
            c=set()
            xy=int(i)
            while xy % 2 == 0:
                c.add(2)
                xy =xy / 2
            for j in range(3, int(math.sqrt(xy))+1, 2):
                while xy % j == 0:
                    c.add(int(j))
                    xy = xy / j
            if(xy>2):
                c.add(int(xy))
            print(i,c)
            prod=functools.reduce(operator.mul, c)
            print(prod)
            
            if(prod==int(i)):
                print("yes")
                count=count+1
    print(count)
n=int(input())
s=list(map(int,input().split()))
fun1(n,s)
