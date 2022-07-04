M, N = list(map(int, input().split()))
for i in range(M, N+1):
  if (i ==1):
    continue
  for j in range(2, int(i**0.5)+1):
    if(i % j == 0):
      break
  else:
    print(i)


#for else문 
#    for문
#    else문
#이 있을 때 else문은 for문이 break없이 온전하게 완료되면 작동한다.
