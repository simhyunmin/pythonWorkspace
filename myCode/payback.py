#거스름돈 계산 코드
def payback(money, price):
  return money-price

money = int(input())
price = 0
showcase = {"사과":100, "파인애플":200, "멜론":500, "키위":1000}

while (True):
  select = input("상품을 선택하세요 100:사과, 200:파인애플, 500:멜론, 1000:키위 0:선택종료\n")
  if(select == "0"):
    break;
  price = price+showcase[select]
  

if(payback(money, price)>=0):
  print(f"계산이 완료되었습니다. 거스름돈 {payback(money, price)}원을 가져가세요")
else:
  print(f"계산실패. {-payback(money, price)}원이 부족합니다.")