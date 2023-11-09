import numpy as np
escalon = lambda x: 0 if x < 0 else 1
p=np.array([[1,1,1],
            [0,1,1],
            [1,1,0],
            [1,1,1],
            [0,1,1],
            [1,0,1],
            [1,0,1],
            [1,1,1],
            [1,1,1],
            [1,1,1]])
p=p.T

tRes=[1,0,1,0,1,0,1,0,1,0]
t=tRes
w=2*np.random.rand(1,3)-1
b=2*np.random.rand(1)-1
e=np.zeros(10)
for epocas in range(500):
    for q in range(len(p)):    
        e[q]=t[q]-escalon(np.dot(w,p[:,q])+b)
        w=w+(e[q]*(p[:,q]).T)
        b=b+e[q]
print("Error:",e)
print("Pesos:",w)
print("Polarizacion:",b)