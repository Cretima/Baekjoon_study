# 명령 프롬프트

''' 끄적끄적
N개의 파일들이 있고 각 파일의 제목 길이(len)는 같다. 
N개의 파일을 서로 비교해 같은부분은 그대로 출력 아닌부분은 ?로 출력한다.
여러 파일들을 입력해도 파일 중 하나만 틀려도 ?를 넣어야 함으로 두개의 파일만 가지고 비교하자.
'''

N = int(input("파일의 개수는: "))

# 처음 파일 입력
a_file = list(input())
a_len = len(a_file)

# 처음꺼 빼고 나머지 파일 입력
for i in range(N-1):
    b_file = list(input())

# 두 파일을 비교 및 서로 다른부분 ?로 변환
for i in range(a_len):
    if a_file[i] != b_file[i]:
        a_file[i] = "?"

print(''.join(a_file)) # 한글자씩 리스트에 들어가 있음으로 '구분자'.join 사용해서 모든 요소를 더해 문자열로 출력

