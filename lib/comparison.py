
"""执行结果比对方法，可以细化执行结果，当执行结果为通过的时候，返回Ture ,失败的时候返回FALSE"""
__author__ = '优秀的北京团队'
def comparison(expected,result):
    str = result


    #print("**查看值**" +str1)
    if expected['result'] in str.content.decode("utf-8"):

        re = True
        print("**执行成功  -->{0}**".format(expected['name']))
        print("页面返回信息：%s" % str.content.decode("utf-8"))
    else:

        re = False
        print("**执行失败  -->{0}**".format(expected['name']))
        print("页面返回信息：%s" % str.content.decode("utf-8"))
    return re