av=[[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,1,0]]
res=list()
col=[]
print(res)
count=0
minc=[]
for i in range(4):
    for j in range(4):
        if av[i][j]==1:
            count=count+1
        
for i in range(4):
    res1=[]
    for j in range(4):
        
        if av[i][j]==0:
            s1=abs(4-i)
            s2=abs(s1-count)
            s3=abs(s2+1)

            res1.append(s3)
        else:
            res1.append(0)
    res.append(res1)
    
print(res)
                
                    



