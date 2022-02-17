# 문자 입력
string2 = str(input("문자를 입력: "))
s2 = string2.split(sep=' ') # 공백 기준으로 문자열 나누기.

# 출력 확인
# print(len(string2)) # 22
print(f"string2.split(sep=' ') : {s2}") # ['sehyun', 'is', 'noob', 'guy']
print(len(s2)) # 단어 확인. 4
