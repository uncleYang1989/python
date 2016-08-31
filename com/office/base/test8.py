# while True:
#     a = int(raw_input());
#     b = int(raw_input());
#     c = int(raw_input());
#      
# #     a,b,c
# #     a,c,b
# 
# #     c,a,b
# #     c,b,a
# 
# #     b,a,c
# #     b,c,a
#     if b > a and a > c:
#         print b, a , c
#     elif b > c and c > a:
#         print b, c , a
#     
# print range(12)
# print range(10,12)
bubbleList = range(3)
print sum(bubbleList)
import time
now = time.time()
# print bubbleList
for i in range(len(bubbleList)):
    for j in range(i+1, len(bubbleList)):
        print "index[%d],value[%d]"%(i,bubbleList[i]) ," compare " + "index[%d],value[%d]"%(j,bubbleList[j]) 
        if bubbleList[i] < bubbleList[j]:
            print "change"
            bubbleList[i],bubbleList[j]=bubbleList[j],bubbleList[i]
            print bubbleList
end = time.time()
print now - end
print bubbleList

