from Case.case import TestCase1
from lib.gettoken import gettoken


def readcase():
    #获取token
    token = gettoken()

    testData = []
    #定义用例数量num，下发添加多少条用例这个值就对应修改到多少。
    num = 3

    # 获取用例列表
    testData1 = TestCase1().userlist(token)
    # 获取敏感词列表
    testData2 = TestCase1().searchwords(token)
    # 获取首页信息
    testData3 = TestCase1().firstpage(token)


    #..........

    names= locals()
    #开始 将testData%i的值进行相加，以便执行
    for i in range(num):

        if i == 0 :
            n = i + 1
            testData = names['testData%s'%n]
            #print("i =1的时候 ")
        else:
            n = i + 1
            testData = testData + names['testData%s'%n]





    #testData = testData1+testData2
    #print("总的list：%s" % testData)
    return testData
