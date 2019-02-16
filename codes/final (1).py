import numpy as np
import matplotlib.pyplot as plt
import math


A=np.array([0,1])
B=np.array([3,-2])
m=np.array([math.sqrt(3),1])
n=np.array([[0,1],[-1,0]]) 
a=np.matmul(n,m.T)
b=a.T

#line passing through B and making 60degrees with given line in anticlockwise direction
d=np.array([[math.cos(2/3.0*math.pi),-math.sin(2/3.0*math.pi)],[math.sin(2/3.0*math.pi),math.cos(2/3.0*math.pi)]])
l=np.dot(d,m.T)
v=l.T
p=np.matmul(n,v)
q=p.T

#line passing through B and making 60degrees with given line in clockwise direction
e=np.array([[math.cos(1/3.0*math.pi),-math.sin(1/3.0*math.pi)],[math.sin(1/3.0*math.pi),math.cos(1/3.0*math.pi)]])
f=np.dot(e,m.T)
g=f.T
h=np.matmul(n,g)
j=h.T
print e

len=10
k=np.linspace(0,5,len)
x=np.zeros((2,len))
x1=np.zeros((2,len))
y=np.zeros((2,len))
y1=np.zeros((2,len))
u=np.zeros((2,len))
u1=np.zeros((2,len))

for i in range(len):
	t=A+k[i]*b
	t1=A-k[i]*b
	x[:,i]=t.T
	x1[:,i]=t1.T
	t2=B+k[i]*q
	t3=B-k[i]*q
	y[:,i]=t2.T
	y1[:,i]=t3.T
	t4=B+k[i]*j
	t5=B-k[i]*j
	u[:,i]=t4.T
	u1[:,i]=t5.T
	
	
plt.axhline(y=0,color='g',label='$y=0$')

plt.plot(x[0,:],x[1,:],color='r',label='$sqrt3x+y=1$')#given line
plt.plot(x1[0,:],x1[1,:],color='r')

plt.plot(u[0,:],u[1,:],color='k',label='$y=-2$')
plt.plot(u1[0,:],u1[1,:],color='k')	

plt.plot(y[0,:],y[1,:],color='c',label='$-sqrt3x+y+2+3sqrt3=0$')
plt.plot(y1[0,:],y1[1,:],color='c' )

plt.plot(B[0],B[1],'o')
plt.text(B[0]*1.2,B[1]*1.2,'B')
plt.grid()
plt.xlabel("$x-axis$")
plt.ylabel("$y-axis$")
plt.legend(loc='best')
plt.axis('equal')
plt.show()
plt.savefig('plot.png')




