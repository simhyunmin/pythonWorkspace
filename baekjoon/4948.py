def prime(n):
  if n == 1:
    return False
  else:
    for i in range(2, int(n**0.5)+1):
      if(n%i == 0):
        return False
    return True
  
numlist = [x for x in range(123456*2+1)]
primeList = []

for i in numlist:
  if(prime(i)):
    primeList.append(i)

while(True):
  N = int(input())
  if(N == 0):
    break
  count = 0
  for i in primeList:
    if(N < i <=2*N):
      count+=1
  print(count)