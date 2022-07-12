import math
def prime(n):
  if n == 1:
    return False
  else:
    for i in range(2, int(n**0.5)+1):
      if(n%i == 0):
        return False
    return True

numlist = [x for x in range(10001)]
primeList = []
for i in numlist:
  if(prime(i)):
    primeList.append(i)

T = int(input())
for _ in range(T):
  i = 0
  N = int(input())
  num = 0
  while primeList[i] <= math.floor(N/2):
    i+=1
  i -=1
  while i>=0:
    num = N-primeList[i]
    if num in primeList:
      break
    i-=1
  print(primeList[i], num)


