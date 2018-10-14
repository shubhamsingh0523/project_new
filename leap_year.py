
year=int(input("Enter any year: "))

if year%4==0:
    if year%400==0:
    	print("YES")
		
    elif year%100==0:
        print("NO")
    print("YES")
else :
    print("NO")
    
