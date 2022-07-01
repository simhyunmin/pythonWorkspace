def checker(str):
  result = []
  for value in str:
    if value not in result:
      result.append(value)
  str2 = "" #str의 단어들을 그룹 단어 형태로 만든 문자열
  for i in result:
    for j in range(str.count(i)):
      str2 = str2+i
  if(str2 == str):
    return True
N = int(input())
count = 0
for i in range(N):
  str = input()
  if(checker(str)):
    count = count+1
print(count)

