# l = range(1,10)
# for i in l:
#     tmp = ""
#     for j in range(1,i+1):
#         tmp += "%d*%d=%d "%(j,i,j*i)
#     print tmp
#     
     
     
# i = 2
# j = 3
# z = 4
# s = str(i) + "*" + str(j) + "=" + str(i*j)  
# s += " " + str(i) + "*" + str(z) + "=" + str(i*z)
#  
# s1 = "%d*%d=%d"%(i,j,i*j)
# s1 += " %d*%d=%d"%(i,z,i*z)
# print s
# print s1
l = range(1,10)
for i in l:
    s = " "
    for j in range(1,i+1):
        s +=  "%d*%d=%d"%(i,j,i*j)
        s +=  " "
    print s
     
