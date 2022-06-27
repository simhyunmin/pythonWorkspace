def hanCounter(k):
  k = str(k)
  k = list(map(int, k))
  if(k[1]-k[0] == k[2]-k[1]):
    return True
  else:
    return False

N = int(input()) # 입력 N
han = 99   #한수의 개수
hanNum = set()
if(N <100):
  han = N
else:
  for i in range(100, N+1):
    if(hanCounter(i)):
      hanNum.add(i)
  han = han+len(hanNum)
print(han)



