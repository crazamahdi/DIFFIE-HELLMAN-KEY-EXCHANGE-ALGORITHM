import random
import math
import socket
l1=[] 
l2=[]
px=[]
k=0
yc=0
host = 'localhost'
port =int(input("Enter port\n"))
def primeNr(n): #storing prime no from 100 to n=1000 in list l1
    for i in range(100,n):
        ip= True
        for j in range(2,int(math.sqrt(i)) + 1):
            if i % j == 0:
                ip= False
                break
        if ip:
            l1.append(i)
primeNr(500)
q=random.choice(l1)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("Prime is:",q)
c.send(str(q).encode())
msg=c.recv(1024)
print(msg.decode())

print("Client Is",str(addr))
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)           
    return roots
l2 = primRoots(q)
a=random.choice(l2)
print("Primitive root is:",a)
c.send(str(a).encode())
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
yc=int(c.recv(1024).decode())
c.send(str(y1).encode())
print("client:",yc)
k=((yc**x1)%q)
print("Secret key is",k)
c.close() 
