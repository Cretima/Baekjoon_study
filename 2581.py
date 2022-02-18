# 지정된 범위안 소수 구하기.

import math

def prime_num(m,n):
    
    if m == 1: # 1은 소수가 될수 없기에
        m += 1
    # 1까지 소수가 없기에 소수가 없다고(-1) 표시해
    if n == 1: 
        return -1

    # n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

    # 에라토스테네스의 체 알고리즘 
    for i in range(m, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근(or n + 1)까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우) 아닌 경우엔 다음 수로 이동

            # i를 제외한 i의 모든 배수를 지우는 부분
            j = 2 
            while i * j <= n:
                array[i * j] = False # 자신(i)을 제외한 i의 배수의 값을 False로 지워
                j += 1
    
    return array # 소수만 남은 배열을 돌려줘


# main
M = int(input("어디부터?(정수): "))
N = int(input("어디까지?(정수): "))


array = prime_num(M, N)

if array == -1:
    print(-1)
else:
    # 정해진 범위의 소수값만(True) 다른 리스트(Sum)에 넣어줘.
    Sum = []
    for i in range(M, N + 1):
        if array[i] == True:
            Sum.append(int(i))


    # 출력(1. 모든 소수의 합 2. 그 중 최솟값 / 소수가 없으면 -1 출력)
    if not Sum: # 소수가 존재하지 않으면
        print(-1)
    else:
        result = 0 # 모든 소수 합
        for j in Sum: # 1.
            result += j
        
        print(result) # 1.
        print(Sum[0]) # 2.
