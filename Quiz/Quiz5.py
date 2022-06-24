from random import *
pas = [randrange(5, 51) for i in range(50)]
counter = 0
for i in range(len(pas)):
  if(5<=pas[i]<=15):
    print(f"[0] {i+1}번째 손님 (소요시간 : {pas[i]}분)")
    counter = counter+1
  else:
    print(f"[ ] {i+1}번째 손님 (소요시간 : {pas[i]}분)")

print(f"총 탑승 승객 : {counter} 분")
