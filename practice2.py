# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5])
# print(cabinet.get(5)) #get을 이용했을 경우에는 값이 없으면 none 출력
# print(cabinet.get(5, "사용 가능")) #get을 이용했을 때 none 대신 다른 값 출력하고 싶으면 (  ," ")
# print("hi")
# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"김태호"}

# print(cabinet["A-3"])
# print(cabinet["B-100"])
# print(cabinet.get("C-20", "사용 가능"))
# cabinet["C-20"] = "조세호"
# print(cabinet["C-20"])

# cabinet["A-3"] = "김종국"
# print(cabinet["A-3"])

# del cabinet["A-3"]
# print(cabinet.get("A-3"))

# print(cabinet)
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())

# cabinet.clear()
# print(cabinet)


#튜플:변경되지 않는 목록, 리스트와 달리 속도가 빨라서 사용

# menu = ("돈까스", "치즈")
# print(menu[1])

# menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# set(집합)
#중복 안됨, 순서 없음
# my_set = {4, 1, 3, 2, 3, 3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# print(java)
# python = {"유재석", "박명수"}

# #교집합
# print(java & python)
# print(java.intersection(python))

# #합집합
# print(java | python)
# print(java.union(python))
# #차집합
# print(java-python)
# print(java.difference(python))

#사람 추가
# python.add("김태호")
# print(python)

# #사람 제거
# java.remove("김태호")
# print(java)

# menu = {"커피", "주스", "우유"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))


# a = input("인사해주십시오\n")

# if(a == "하이"):
#   print("반갑습니다.")
# elif(a == "바이"):
#   print("안녕히 가십시오")
# else:
#   print("다시 입력해")

# for waiting_no in [0, 1, 2, 3, 4]:
#   print(f"대기번호 : {waiting_no}")


# for waiting_no in range(1, 6):
#   print(f"대기번호 : {waiting_no}")

# list = ["1", "2", "3"]
# for num in list:
#   print("1"+num)

#whule
# customer = "손님"
# index = 5
# while index >= 1:
#   print(f"{customer}, 커피가 준비되었습니다. {index} 번 남았어요.")
#   index-=1
#   if index == 0:
#     print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#   print(f"{customer} 커피가 준비되었습니다. 호출 {index}회")
#   index +=1

# customer = "손님1"
# person = "Unknown"
# while person != customer:
#   print(f"{customer}, 커피가 준비 되었습니다.")
#   person = input("이름이 어떻게 되세요?")
#   if(person == customer):
#     print("맛있게 드세요 ^_^")

# def sum100(x):
#   return x+100
# def lenp(x):
#   return len(x)
# students = list(map(sum100, [1, 2, 3, 4, 5]))
# print(students)
# student = list(map(lenp, ["jully", "happy", "sad", "mountain", "good"]))
# print(student)


















