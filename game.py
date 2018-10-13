import random
print('\n 0=scissor \n 1=rock \n 2=paper\n')
c=[0,1,2]
n=random.choice(c)
u=int(input("enter a number"))
if(u==n):
	r='draw'
elif((u==0 and n==1)or(u==1 and n==2)or(u==2 and n==0)):
	r='computer wins'
else:
	r='user wins'

print('user entered=',u)
print('computer entered=',n)
print(r)