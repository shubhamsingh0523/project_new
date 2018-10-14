N=int(input("enter value of N: " ))
K=int(input("enter value of K: " ))
if K>N :
   print("invalid inputs")
else:  
     sum=0
     arr=[] 
     print("enter array: ")
     for x in range(N):
	     arr.append(int(input()))
     for i in range(K):
         sum = sum + arr[i]
     print("\n sum is ")
     print(sum)	 