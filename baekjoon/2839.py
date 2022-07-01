# from operator import mod


# N = int(input())
# p = 0  #5 몇 번 나누는지 세리는 변수
# q = 0  #3 몇 번 나누는지 세리는 변수
# counter = 0
# numlist = []
# for i in range(0, (N // 5)+1):
#   num = N
#   if(i >0):
#     num = N -(5*i)
#     p = i
#   if(num %3 == 0):
#     q = num // 3
#     numlist.append(p+q)
#     counter += 1
# if(counter == 0):
#   print(-1)
# else:
#   print(min(numlist))

# amount = int(input())

# def check(a):
#     for i in range(amount // 5, -1, -1):   # 5로 나눌 수 있는 최대 몫부터 시작해서 따로 min 찾을 필요가 없음
#         if (amount - i*5) % 3 == 0:
#             print(i + (amount - i*5) // 3)
#             return 1
#     return -1

# if check(amount) < 0:
#     print(-1)
