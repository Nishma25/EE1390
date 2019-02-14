import numpy as np
import matplotlib.pyplot as plt

len=75

def intersect():
	n1=np.array([2,1])
	n2=np.array([1,-1])
	N=np.vstack((n1,n2))
	p=np.array([3,1])
	return np.matmul(np.linalg.inv(N),p) # given ON=p => O=(N^-1)p

O=intersect() #intersection point
print(O)
A=np.array([1,-1])#point on circle at which tangent is drawn 
OA=A-O
print(OA)# directional vector of line joining O and A
k=np.array([[0,1],[-1,0]]) 
t=np.matmul(OA,k)
a=t.T
print(a)

l=np.linspace(0,2,75)
m=np.zeros((2,75))
n=np.zeros((2,75))
for i in range(len):
	t=A+l[i]*(a)
	t1=A-l[i]*(a)
	m[:,i]=t.T
	n[:,i]=t1.T

plt.plot(m[0,:],m[1,:],label="$T$") #{x,y/x>1,y<-1}
plt.plot(n[0,:],n[1,:],label="$T1$")#{x,y/x<1,y>-1}
plt.plot(O[0],O[1],'o')
plt.text(O[0]*1.1,O[1]*1.1,'O')
plt.plot(A[0],A[1],'o')
plt.text(A[0]*1.1,A[1]*1.1,'A')

r=np.linalg.norm(OA)#radius
def Circle(i):
	A=O+(r)*(np.array([np.cos(i),np.sin(i)])) #circle = centre + radius(cosi+sini) 


c=plt.Circle((O[0],O[1]), r , color='r', fill=False) # Circle with centre 'O',radius= OA
plt.gca().add_artist(c) #plotting circle 
plt.grid()
plt.xlabel("$x-axis$")
plt.ylabel("$y-axis$")
plt.legend(loc='best')
plt.axis('equal')
plt.show()
plt.savefig('plot.png')
