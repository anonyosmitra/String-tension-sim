import math
import matplotlib.pyplot as plt
import numpy as np
t=[]
ep=[]
ek=[]
ec=[]
l=math.pi
n=10
dx=l/n
dt=0.2
y=[]
v=[]
a=[]
y2=[]
v2=[]
a2=[]

def inputE():
    #=(G8-F8)^2/(2*dx)
    #=dx * G9 ^ 2 / 2
    global ep,ek,ec
    p=0
    k=0
    for i in range(1,10):
        p+=math.pow((y[i]-y[i-1]),2)/(2*dx)
        k+=dx*math.pow(v[i],2)/2
    ep.append(p)
    ek.append(k)
    ec.append(p+k)

t.append(0)
for i in range(0,11):
    y.append(math.sin(dx*i))
    v.append(0)
a.append(0)
for i in range(1,10):
    a.append((y[i-1]-2*y[i]+y[i+1])/math.pow(dx,2))
a.append(0)
for i in range(0,11):
    y2.append(y[i]+v[i]*dt/2)
    v2.append(v[i]+a[i]*dt/2)
    a2.append(-y2[i])
inputE()


for j in range(1,15):
    t.append(j)
    for i in range(0,11):
        y[i]+=v2[i]*dt
        v[i]+=a2[i]*dt
        a[i]=-y[i]
        y2[i]=(y[i] + v[i] * dt / 2)
        v2[i]=v[i] + a[i] * dt / 2
        a2[i]=-y2[i]
    inputE()
plt.plot(np.array(t),np.array(ep))
plt.plot(np.array(t),np.array(ek))
plt.plot(np.array(t),np.array(ec))
plt.show()



