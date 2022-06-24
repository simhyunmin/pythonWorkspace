dic = {1:"hi", 5:"bye", 7:"goodnight"}

while(True):
  key = int(input())
  value = input()

  if(key in dic):
    dic[key+1] = value
  else:
    dic[key] = value
  print(dic)