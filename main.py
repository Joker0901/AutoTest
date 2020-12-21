
import unittest,requests,ddt
from lib.sendrequests import SendRequests
from lib.readcase import readcase
from lib.comparison import comparison
from lib.writreport import createbook, writebook

testData = readcase()
print("生成测试用例数据成功：%s" % testData)
bookname = createbook()
print("bookname：%s" % bookname)

@ddt.ddt
class Demo_API(unittest.TestCase):
    """发布会系统"""
    alldata= []
    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    @ddt.data(*testData)
    def test_api(self, data):
        # 获取ID字段数值，截取结尾数字并去掉开头0
        #print("i = %s" %x)

        print("******* 准备执行用例 ->{0} *********".format(data['name']))
        print("请求方式: {0}，请求URL: {1}".format(data['method'],data['url']))
        print("请求头: {0}".format(data['headers']))
        print("post请求body类型为：{0} ,body内容为：{1}".format(data['type'], data['body']))

        # 发送请求
        print("****RUN****")
        re = SendRequests().sendRequests(self.s,data)
        # 获取服务端返回的值
        self.result = re.json()


        #比对执行结果
        bl = comparison(data,re)
        #print ("执行结果123  ：%s" %result)
        print("预期结果  -->  {0}".format(data['result']))
        if bl:

            redict = dict(zip(["name", "method", "url", "result", "Response"],
                            [data['name'], data['method'], data['url'], "测试通过", re.content.decode("utf-8")]))
            reportbl =  writebook(bookname,redict)
            print("测试报告： %s" %reportbl)

        else:

            redict = dict(zip(["name", "method", "url", "result", "Response"],
                              [data['name'], data['method'], data['url'], "测试通过", re.content.decode("utf-8")]))
            reportbl = writebook(bookname, redict)
            print("测试报告： %s" % reportbl)



    #print("dict = %s" %dict)

if __name__=='__main__':
    unittest.main()
