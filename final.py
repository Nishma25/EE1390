import numpy as np
import matplotlib.pyplot as plt
import math


A=np.array([0,1])
B=np.array([3,-2])
m=np.array([math.sqrt(3),1])
n=np.array([[0,1],[-1,0]]) 
a=np.matmul(n,m.T)
b=a.T

d=np.array([[math.cos(2/3.0*math.pi),-math.sin(2/3.0*math.pi)],[math.sin(2/3.0*math.pi),math.cos(2/3.0*math.pi)]])
l=np.dot(d,m.T)
v=l.T
p=np.matmul(n,v)
q=p.T

len=10
k=np.linspace(0,5,len)
x=np.zeros((2,len))
w=np.zeros((2,len))
y=np.zeros((2,len))
z=np.zeros((2,len))
for i in range(len):
	t=A+k[i]*b
	t1=A-k[i]*b
	x[:,i]=t.T
	z[:,i]=t1.T
	u=B+k[i]*q
	u2=B-k[i]*q
	y[:,i]=u.T
	w[:,i]=u2.T
	
	
plt.axhline(y=0)
plt.axhline(y=-2)	
plt.plot(x[0,:],x[1,:],label='$sqrt3x+y=1$')
plt.plot(y[0,:],y[1,:],label='$-sqrt3x+y+2+3sqrt3=0$')
plt.plot(w[0,:],w[1,:])
plt.plot(z[0,:],z[1,:])
plt.plot(B[0],B[1],'o')
plt.text(B[0]*1.2,B[1]*1.2,'B')
plt.grid()
plt.xlabel("$x-axis$")
plt.ylabel("$y-axis$")
plt.legend(loc='best')
plt.axis('equal')
plt.show()
plt.savefig('plot.png')




