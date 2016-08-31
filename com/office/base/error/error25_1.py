#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
'''
【程序25】 
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。 

'''

def isHuiWen(i):
    s = str(i)
    if s[0] == s[4] and s[1] == s[3]:
        return True
    else:
        return False

'''
10001 is huiwen
10101 is huiwen
10201 is huiwen
10301 is huiwen
10401 is huiwen
10501 is huiwen
10601 is huiwen
10701 is huiwen
10801 is huiwen
10901 is huiwen
11011 is huiwen
11111 is huiwen
11211 is huiwen
11311 is huiwen
11411 is huiwen
11511 is huiwen
11611 is huiwen
11711 is huiwen
11811 is huiwen
11911 is huiwen
12021 is huiwen
12121 is huiwen
12221 is huiwen
12321 is huiwen
12421 is huiwen
12521 is huiwen
12621 is huiwen
12721 is huiwen
12821 is huiwen
12921 is huiwen
13031 is huiwen
13131 is huiwen
13231 is huiwen
13331 is huiwen
13431 is huiwen
13531 is huiwen
13631 is huiwen
13731 is huiwen
13831 is huiwen
13931 is huiwen
14041 is huiwen
14141 is huiwen
14241 is huiwen
14341 is huiwen
14441 is huiwen
14541 is huiwen
14641 is huiwen
14741 is huiwen
14841 is huiwen
14941 is huiwen
15051 is huiwen
15151 is huiwen
15251 is huiwen
15351 is huiwen
15451 is huiwen
15551 is huiwen
15651 is huiwen
15751 is huiwen
15851 is huiwen
15951 is huiwen
16061 is huiwen
16161 is huiwen
16261 is huiwen
16361 is huiwen
16461 is huiwen
16561 is huiwen
16661 is huiwen
16761 is huiwen
16861 is huiwen
16961 is huiwen
17071 is huiwen
17171 is huiwen
17271 is huiwen
17371 is huiwen
17471 is huiwen
17571 is huiwen
17671 is huiwen
17771 is huiwen
17871 is huiwen
17971 is huiwen
18081 is huiwen
18181 is huiwen
18281 is huiwen
18381 is huiwen
18481 is huiwen
18581 is huiwen
18681 is huiwen
18781 is huiwen
18881 is huiwen
18981 is huiwen
19091 is huiwen
19191 is huiwen
19291 is huiwen
19391 is huiwen
19491 is huiwen
19591 is huiwen
19691 is huiwen
19791 is huiwen
19891 is huiwen
19991 is huiwen

'''