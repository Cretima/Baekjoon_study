# 두 수의 최대공약수와 최소공배수

num1 = int(input("첫번째 수: "))
num2 = int(input("두번째 수: "))
n = num2
max_num = 0 # 최대공약수
mini_num = 0 # 최소공배수


if num1 < num2:
    n = num1

# num1(60)의 약수 찾기
while True:
    if n == 1:
        break

    result = num1 % n

    if result != 0: # 나머지가 생기면 약수가 아니야
        n -= 1
        continue

    # 나머지가 없으면 num2(45)도 같은 약수로 나눠줘
    else:
        result = num2 % n
        if result != 0:
            n -= 1
            continue
    max_num = n # 제일 처음 나온 공약수가 최대공약수일거야
    break


mini_num = max_num * (num1 // max_num) * (num2 // max_num) # 최소공배수 공식
print(f"{max_num} {mini_num}")
