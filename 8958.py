n = int(input())
for _ in range(n): # 5번 반복해줘 
    count = 0 # 연속 정답으로 인한 점수 구분 변수
    result = 0
    problem = list(input())
    for i in problem: # 입력된 문제 줄 만큼 반복
        if i == 'O': # 만약 맞은 문제면
            count += 1 # 점수를 1점 추가해
            result += count # 총 점수에 맞은 문제의 점수를 추가해
        else:
            count = 0 # 틀리면 점수 초기화
    print(result)