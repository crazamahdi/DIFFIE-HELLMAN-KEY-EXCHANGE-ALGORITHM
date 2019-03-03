import random
import math
import socket
l1=[] 
l2=[]
px=[]
k=0
q=0
a=0
ys=0
host = 'localhost'
port =int(input("Enter port\n"))
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
q=int(s.recv(1024).decode())
print("Prime :",q)
s.send(b"Send primitive root")
a=int(s.recv(1024).decode())
print("Primitive root:",a)
def pno(q):
    i=0
    x=0
    for i in range(q):
        px.append(i)
    x=random.choice(px)
    return x
x1=pno(q)
print("private component:",x1)
def public_component(q,a,x1):
    y=0
    y=((a**x1)%q)
    #print("public comp is",y)
    return y
y1=public_component(q,a,x1)
print("public component:",y1)
s.send(str(y1).encode())
ys=int(s.recv(1024).decode())
print("Server:",ys)
k=((ys**x1)%q)
print("Secret key is",k)
s.close()               
