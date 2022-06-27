T = int(input())
for i in range(T):
  list = []
  R,S =input().split()
  R = int(R)
  for x in S:
    for y in range(R):
      list.append(x)
  print(''.join(list))