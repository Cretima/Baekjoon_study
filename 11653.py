# 소인수분해 프로그램
num = 60

# N = int(input())

i = 2
while num != 1 :
    if num % i == 0 :
        num = num//i
        print(i)
    else :
        i += 1
