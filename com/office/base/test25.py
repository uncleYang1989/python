
def isHuiWen(i):
    s = str(i)
    if s[0] == s[4] and s[1] == s[3]:
        return True
    else:
        return False

for i in range(10000,100000):
    result = isHuiWen(i)
    if result:
        print "is  huiwen ", i
    else:
        print "is not huiwen" , i
