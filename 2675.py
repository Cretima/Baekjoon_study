def made_list(string, num): # 실행 함수
    string1 = list(string) # 받은 문자열을 리스트로 저장해 ABC -> ['A', 'B', 'C']

    n = 0
    while(n < len(string1)): # 리스트에 있는 인덱스를 하나씩 꺼내서 string1만큼 반복할거야
        string1[n] = string1[n] * num # n 번째 인덱스를 num 반복으러 찍고 다시넣어 
        print("확인겸 출력")
        print(string1[n])# 출력 확인용이야
        n += 1
    return string1

def result_str(string): # 결과 출력함수
    result = ''.join(string) # 리스트에 있는 모든 인덱스를 문자열로 합쳐줘(''.join)
    print(result) # 결과를 출력


# main
string1 = "ABC"
string2 = "/HTP"

num = 2 # 한문자를 몇번 반복할꺼야? 

result1 = made_list(string1, num)
result_str(result1)

result2 = made_list(string2, num)
result_str(result2)
