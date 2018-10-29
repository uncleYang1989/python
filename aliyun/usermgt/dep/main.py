#!/usr/bin/python
# encoding=utf8
'''
Created on 2018年8月10日

@author: jyang
'''
from aliyun.usermgt.dep.createDefaultPerms import importPerms
from aliyun.usermgt.dep.createDefaultRoles import importRoles
from aliyun.usermgt.dep.createOrgTree import installOrgs
from aliyun.usermgt.dep.createDefaultUsers import importUser

if __name__ == '__main__':
#     importPerms();
#     roleMap = importRoles();
#     installOrgs();
#     importUser(roleMap);
    sss = """
        b25c50e1e9dba3e6af2d0acf4b9533a5;全市域;10;3
    c52d33de1c3f61330bf198b92c6e9c45;市区;20;3
    ffedf6c1c30a48c3946bb7c2273651e9;主城区;30;1
    6301f9905d6ffa1412ac94c82a6e79ab;上城大队;40;2∑
    16c0ea42c2ec7bf092f87abb4a5d3924;下城大队;50;2
    2fc5e60107ebdbca0d036ad2f2e2671f;西湖大队;60;2
    efbbe65ee090be44c43d6abc651c9db5;江干大队;70;2
    ebbd32f29fd5497bb562578ee56eb750;拱墅大队;80;2
    ebe1ff7e9ba13167dde50b4b1fb238ac;滨江大队;90;2
    6767c2b7de2284b9bfaad561007efcd2;下沙大队;100;2
    7bf53803e110904f76f0268ebba7742e;高架大队;110;5
    5f72cd90551e21fee79a57c88c02c5e1;绕城大队;120;6
    baddbf886e3cb1bbdd6faef29f70d380;景区大队;130;2
    bf89db7c6bca207dc0da6715dee1426d;大江东大队;140;4
    d9ff8785ee954676e58c4c8f87069942;萧山大队;150;4
    2b5fb1dccfb3325b034ed443a3489520;余杭大队;160;4
    ab3475fd39c845022df5ee9b1415087a;富阳大队;170;4
    4b2ed4f5d4853506afbadaaf25bc8d63;临安大队;180;4
    a52a141ddabf96f18282491511096c5e;桐庐大队;190;4
    bdc6a5b7d58c9af5add3fb5728caba9c;淳安大队;200;4
    26420f1fdfe4d8810e0356a9097ec4d5;建德大队;210;4""".strip().split("\n")
    for ss in sss:
        print ss.split(";")[1]
    
全市域:
上城大队
下城大队
西湖大队
江干大队
拱墅大队
滨江大队
下沙大队
高架大队
绕城大队
景区大队
大江东大队
萧山大队
余杭大队
富阳大队
临安大队
桐庐大队
淳安大队
建德大队

市区:
上城大队
下城大队
西湖大队
江干大队
拱墅大队
滨江大队
下沙大队
高架大队
绕城大队
景区大队
大江东大队
萧山大队
余杭大队
富阳大队
临安大队

主城区:
上城大队
下城大队
西湖大队
江干大队
拱墅大队
滨江大队
下沙大队
高架大队
绕城大队
景区大队