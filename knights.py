n = 9
s1,c1,s2,c2=4,0,0,0
d ={}
ifFound =0
maxVal=10000
def ifNeighbour(x,y):
    f=1
    if x<0 or y<0 or x>=n or y>=n:
        f=0
    return f

def addToArr(x,y,c,arr):
    global maxVal,ifFound
    f=0
    if ifNeighbour(x,y):
        if x == s2 and y == c2:
            ifFound=1
            if maxVal > c+1:
                maxVal=c+1
        else:
            arr.append([x,y,c+1])
            f=1
    return f
def findMin():
    keyArr=[]
    vis={}
    x=s1
    y=c1
    k = [x,y,0]
    d = str(s2)+'-'+str(c2)
    keyArr.append(k)
    l=1
    
    while l!=0:
        k = keyArr.pop(0)
        l-=1
        x,y,c=k[0],k[1],k[2]
        if str(x)+'-'+str(y) not in vis:
            if addToArr(x+1,y+2,c,keyArr):
                l+=1
            if addToArr(x+1,y-2,c,keyArr):
                l+=1
            if addToArr(x-1,y+2,c,keyArr):
                l+=1
            if addToArr(x-1,y-2,c,keyArr):
                l+=1
            if addToArr(x+2,y+1,c,keyArr):
                l+=1
            if addToArr(x+2,y-1,c,keyArr):
                l+=1
            if addToArr(x-2,y+1,c,keyArr):
                l+=1
            if addToArr(x-2,y-1,c,keyArr):
                l+=1
            vis[str(x)+'-'+str(y)]=1
findMin()
if ifFound:
    print(maxVal)
else:
    print(-1)