# print(5>10)
# print(5<10)
# print(not False)
# print(not(5+6>10))
# #애완동뭉을 소개해 주세요
# '''
# 안녕하세요
# 반갑습니다
# 굿
# '''
# # bye
# # hi
# name = '연탄이'
# animal = "강아지"
# age = 4
# hobby = "산책"
# is_adult = age >= 5
# print("우리집 "+animal+"의 이름은 "+name+"이에요")
# print(''+name+'는 '+str(age)+'살이며, '+hobby+'을 아주 좋아해요')
# # print(''+name+'는 ',age,'살이며, '+hobby+'을 아주 좋아해요')
# print(''+name+'는 어른일까요? ',is_adult)

# print(not(1 != 3) is not(1 >= 0))
# print(1 is 3)

# print((9>8) or (3<=2))

# print((3>0)&(2>1))

# print((3<4) or (2>4))
# print((3>4) | (4>3))

# number = 2*3+4
# number = number+2
# print(number)

# print(abs(-5))

# print(pow(2,63))
# print(max(5, 4))
# print(min(5, 4))
# print(round(3.89))

# from math import *
# from tokenize import Double
# num = input()
# num = float(num)
# print(floor(num))
# print(ceil(3.14))
# print(sqrt(16))
# print(ceil(3.14))
# print(sqrt(3))

# from random import *
# num = random()
# print(int(num*10)+1) 
# print(int(num*10)+1)  
# print(int(num*10)+1)  
# print(int(num*10)+1)    
# print(int(num*10)+1)  
# print(int(num*10)+1)  
# print(int(num*10)+1)  

# print(int(random()*45)+1)

# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))

# print(randint(1, 45))

# import random
# num = random.randrange(1, 11)
# print(num)
# from random import *
# num1 = random()
# print(num1)
# print(randrange(1, 3)) #1~3미만의 임의의 값 생성
# sentence2 = "나는 소년입니다."
# sentence1 = '파이썬은 쉬워요'
# sentence3 = """
# 나는 소년이고, 파이썬은
# 쉬우
# """

# print(sentence3)
# print(sentence1, sentence2)

# jumin = "990120-1234567"

# print("성별 : "+ jumin[7])
# print("연 : "+jumin[0:2])
# print("월 : "+jumin[2:4])
# print("일 : "+jumin[4:6])
# print("생년월일 : "+jumin[0:])
# print("생년월일 : "+jumin[:14])
# print("뒤 7자리"+ jumin[-7:])

# python = "Python isn Amnazing"
# print(python.lower())
# print(python.upper())
# print(python[0].islower())
# print(len(python))
# print(python.replace("is", "are"))
# print(python)
# index = python.index("n")
# print(index)
# index = python.index("n", index+1)
# python = input()
# subs = input()
# python = python.lower()
# index = python.find(subs)
# i = 0
# if(index != -1):
#   i = 1
#   if(index):
#     while index !=len(python)-1:
#       index = python.find(subs, index+1, len(python)+1)
#       if(index == -1):
#         break
#       i = i+1
#   print(i)
# else:
#   print(i)

# print(python.count(subs))
# p = "hi my name is simhyunmin"
# print(p.count("i"))
# print(["ox", "ox", "o", "oxoxox"].count("ox"))

# print("나는 %d살입니다." %20)
# print("나는 %s을 좋아하는 청년입니다." % "파이썬")
# print("Apple 은 %c로 시작합니다." % "A")

# print("나는 %s색과 %s색을 좋아하는 %d살 청년입니다." % ("파랑", "빨간", 20))

# print("나는 {}살입니다.".format(20))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# for a in range(1, 10):
#   for b in range(1, 10):
#     print("{0} x {1} = {2} " .format(a, b, a*b))

# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color="빨간"))

# color = input()
# age=input()
# name=input()
# print(f"나는 {color}색을 좋아하는 {age}살 {name}입니다.")

# print("나는 자처한다\n공부를.")
# print("나는 \"사랑한다\"공부하는 것을")
# print("나는 \'지키는\' 환경 프로젝트의 일원이다.")
# print("C:\\Users\\SAMSUNG\\Desktop\\PythonWorkSpace")

# \r 이후에 오는 문장은 이전 문장이 다 적힌 이후, 커서를 앞으로 보냈을때 다시 작성한 결과를 저장해준다.
# str = input()
# a = 0
# for x in range(len(str)):
#   if(str[x] == " "):
#     break
#   a = a+1
# print(a)
# substr =input()
# substr = substr[0:a]
# print(f"{str}\r{substr}")
# print(str)


# str = input()
# p_backspace = input()
# p_backspace = int(p_backspace)
# str = str[:p_backspace] + "\b" + str[p_backspace:]
# print(str)

# str1 = "hi"
# str2 = "name is simhyunmin"
# str3 = str1+" my "+str2
# print(str3)


# my_string = 'Hello, what are doing?'
# index = my_string.find('doing')
# final_string = my_string[:index] + 'you ' + my_string[index:]
# print(final_string)

# str = "hi my name is simhyunmin"
# index = str.find("simhyunmin")
# print(index)

# print("red\tapple")

# subway1 = 10
# subway2 = 20
# subway3 = 30
# subway = [subway1, subway2, subway3]
# subway = ["1", "2", "4354"]
# print(subway[2].index("5"))

# subway = ["1", "2", "3"]
# subway.append("4")
# print(subway)
# subway.insert(2, "2.5")
# print(subway)

# print(subway.pop())
# print(subway)

# subway.append("3")
# print(subway.count("3"))

# num_list = [5, 4, 2, 1, 3]
# print(num_list)
# num_list.reverse()
# print(num_list)
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)
# num_list.clear()
# print(num_list)

# mix_list = ["조세호", 1, True]
# print(mix_list)

# num_list.extend(mix_list)
# print(num_list)

def func_double(x):
  return x*5

result1 = list(map(int, [1.1, 2.2, 3.3, 4.4]))
print(result1)

result2 = list(map(func_double, [1, 2, 3, 4, 5]))
print(result2)























