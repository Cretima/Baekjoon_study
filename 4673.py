# d(35) = 35 + 3 + 5 

origin_num = set(range(1,1001)) # 1 ~ 1000까지 생성
generat_num = set() # 생성자  # set은 생성자를 만들때 중복을 없애기 위해.
self_num = set()

for i in range(1, 1001): # ex) i = 345
    for j in str(i): # j = '3''4''5' 총 3개를 받아서 >> 3번 반복
        i += int(j) # i = 345 + 3, i = 348 + 4, i = 352 + 5 ---> i = 357
    generat_num.add(i) # 집합형이니 .add / not .append(리스트)

self_num = sorted(origin_num - generat_num) # 셀프 넘버 = 전체 숫자 - 생성자

for i in self_num: # 셀프 넘버 변수 수만큼 반복해
    print(i) # 출력!
