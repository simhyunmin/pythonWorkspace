def d(n):
  sum = n
  for i in str(n):
    sum = sum+int(i)
  return sum

self_num = set(range(1, 10001))
generated_num = set()
for i in range(1, 10001):
  generated_num.add(d(i))

self_num = sorted(self_num - generated_num)
for i in self_num:
  print(i)


