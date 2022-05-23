subject = int(input())
maxnum = 0
result = 0

a_list = list(map(int, input().split()))

maxnum = max(a_list)

for i in range(subject):
   result += (a_list[i] / maxnum * 100)

result /= subject
print(result)


# [3 40 80 60]
 # for i in range(a_list[0]):  
