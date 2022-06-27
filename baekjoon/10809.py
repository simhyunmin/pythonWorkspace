str = input()
str = str.lower()
alpha = [i for i in range(0, 26)]
for i in alpha:
  i = i+ord("a")
  i = chr(i)
  print(str.find(i), end=" ")
