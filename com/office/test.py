# -*- coding: utf-8 -*-

for n in range(1,7):
    youxiao=3.00
    wuxiao=3.00
    print u"取几个:",n
    reuslt = 1.0;
    while n > 0:
        n -= 1
        if youxiao == 0:
            reuslt= 0
            continue
        reuslt = reuslt*(youxiao/(youxiao+wuxiao))
        youxiao -=1
    print u"概率:",reuslt*100,"%"