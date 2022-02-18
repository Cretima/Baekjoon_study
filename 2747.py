# 피보나치 수 n 번째 수 구하기

F = [0,1]

n = int(input("n을 입력하세요(1<n<46): ")) # 몇번째 피보나치 수를 구할거니

for i in range(n): # n번 만큼 반복해
    if i == 0: # 만약 0번째면 1번째로 옮겨줘.(리스트 범위를 초과하기에.)
        continue
    a = F[i] + F[i-1] # i+1값을 a에 저장해줘
    F.append(a) # a값을 리스트 맨뒤에 추가해

result = F[n-1] # 결과를 출력. n-1인 이유는 리스트가 0항 부터 시작하기에.

print(result) # 결과 출력!
