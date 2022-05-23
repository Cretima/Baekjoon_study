
testcase = int(input())

for _ in range(testcase):
    lst = list(map(int, input().split()))
    averge = sum(lst[1:]) / lst[0]

    a = 0
    for i in lst[1:]:
        if i > averge:
            a += 1
       
    result = a / lst[0] * 100
    print("%7.3f" %(round(result, 3)))
    


    

            
            
    
    
    

    


    
    
    


    

    

    




    
        
