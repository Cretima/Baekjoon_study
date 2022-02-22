# 1026 보물

'''
끄적끄적
최솟값을 구하기 위해선 두 배열의 가장 높은수와 낮은 수를 곱해서 더해야 나와
B 배열은 정렬을 할 수 없기에 높은 수의 위치를 찾고 값을 빼서 따로 넣을거야.
'''

N = int(input("배열 크기: "))
# 입력한 값이 정수로 변환해야하니 map 함수를 이용해
A = list(map(int, input("A: ").split(' ')))
B = list(map(int, input("B: ").split(' ')))
print(B)
result = 0

A.sort() # A 배열을 정렬해(오름차순으로)
for i in range(N):
    # 가장 낮은 A 인덱스와 가장 높은 B 인덱스를 꺼내
    a = A[i]
    b = B.pop(B.index(max(B)))

    result = result + (a * b) # S를 구하기 위한 식이야
    
print(result)
