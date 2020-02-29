import pexpect
import time

child_server = pexpect.spawn('./server')
#print("a")
#m=[10,20,30,40,50]

#for n in m:
n=100
l=[]
for i in range(n):
    l.append(pexpect.spawn('./client'))
#print("a")
l[n-10].expect('Connection established ............')
#print("a")
start = time.time()
l[n-10].sendline('SEND hello')
#print("a")
l[n-7].expect('hello')
#print("a")
end = time.time()
print(end - start)


#print("fine")
