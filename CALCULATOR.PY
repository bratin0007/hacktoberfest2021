a=int(input())
while a:
    if a==1:        
        x=int(input())    
        y=int(input())
        print(x+y)
        a=int(input())    
    elif a==2:    
        x=int(input())    
        y=int(input())
        print(x-y)
        a=int(input())
    elif a==3:
        x=int(input())    
        y=int(input())
        print(x*y)
        a=int(input())
    elif a==4:        
        x=int(input())    
        y=int(input())
        print(x//y)
        a=int(input())
    elif a==5:        
        x=int(input())    
        y=int(input())
        print(x%y)
        a=int(input())
    elif a==6:
        exit()
    else:
        print("Invalid Operation")
        a=int(input())