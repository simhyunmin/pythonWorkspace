#몇 번 째 줄인지 알야아하고
#몇 번 째 줄에서 몇 번 째 인덱스에 해당하는지 알아야한다.

#홀수 라인에서는 시작점에서 끝점까지 분모는 증가, 분자 감소, 끝점 분수: 1/line
#짝수 라인에서는 시작점에서 끝점까지 분모는 감소, 분자는 증가, 끝점 분수: line/1
N  = int(input())
index = 0
line = 0
end = 0
while N>end:
  line += 1
  end +=line
if(line % 2 == 0):
  index = end-N
  print(str(line-index)+"/"+str(1+index))
else:
  index = end-N
  print(str(1+index)+"/"+str(line-index))


