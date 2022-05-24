# 단어 공부

# set 함수

eng = input().lower() # Mississipi
eng_word = list(set(eng)) # [m, i ,s, p]
cnt=[]

for i in eng_word: # i = 0, m 
    count = eng.count(i)
    # print(count)
    cnt.append(count) # 1, 4, 4, 1

if cnt.count(max(cnt)) != 1:
    print("?")
else:
    print(eng_word[cnt.index(max(cnt))].upper())




