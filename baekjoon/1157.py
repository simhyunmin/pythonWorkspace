# a = input() 
# a = a.lower()
# b=[0 for i in range(26)]
# for i in range(len(a)):
#   b[ord(a[i])-ord('a')] = b[ord(a[i])-ord('a')]+1

# maxl = b[0]
# indexl = 0

# for i in range(len(b)):
#   if(maxl <= b[i] ):
#     maxl = b[i]
#     indexl = i
    
# maxr = b[len(b)-1]
# lenB = len(b)-1
# indexr = len(b) -1

# while (lenB >= 0):
#   if(maxr <=b[lenB]):
#     maxr = b[lenB]
#     indexr = lenB
#   lenB = lenB-1

# if(indexl == indexr):
#   print(chr(indexl+97).upper())
# else:
#   print("?")

# s = input().upper()
# us =list(set(s))
# print(us)
# count_list =[]
# for i in us:
#   count_list.append(s.count(i))
# if count_list.count(max(count_list))>1:
#   print("?")
# else:
#   print(us[count_list.index(max(count_list))])

