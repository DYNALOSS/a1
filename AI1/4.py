import random
import math

def minimax(cd,ni,maxt,scr,td):
    if(cd==td):
        return scr[ni]
    if(maxt):
        return max(minimax(cd+1,ni*2,False,scr,td),minimax(cd+1,ni*2+1,False,scr,td))
    else:
        return min(minimax(cd+1,ni*2,True,scr,td),minimax(cd+1,ni*2+1,True,scr,td))


scr=random.sample(range(1,50),4)
print(str(scr))
td=math.log(len(scr),2)
print("The Optimal value is ",end=" ")
print(minimax(0,0,True,scr,td))