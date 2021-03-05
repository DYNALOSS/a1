minimum,maximum=-1000,1000
def alphabeta(d,n,maxP,scr,A,B):
    if(d==3):
        return scr[n]
    if maxP :
        best=minimum
        for i in range(0,2):
             value=alphabeta(d+1, n*2+i, False, scr,A,B)
             best=max(best,value)
             A=max(A,best)
             if(B<=A):
                break
        return best
    else :
        best=maximum
        for i in range(0,2):
             value=alphabeta(d+1, n*2+i, True, scr,A,B)
             best=min(best,value)
             B=min(B,best)
             if(B<=A):
                break
        return best
        




scr=[]
x=int(input("Enter no of Leaf nodes"))
for i in range(x):
    y=int(input("Enter the value of leaf node"))
    scr.append(y)

d=int(input("Enter the depth value:"))
n=int(input("Enter the node value:"))

print("The optimal value is ", alphabeta(d,n,True,scr,minimum,maximum))