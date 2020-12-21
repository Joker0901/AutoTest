import unittest
import requests

from lib.readreport import  ReadReport
from lib.sendmail import send_mail



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    def test_api(self):
        path ='D:\Work\Python\AutoTest\Report\测试报告20201218_170609.xlsx'
        testData = ReadReport(path).read_data()
        re = send_mail(testData)
        # re = gettoken()
        # re = "access_token=" + re
        # print("获取到的token：%s" % re)
        # result = comparison(data['result'], re)
        # testData = TestCase1().userlist()
        # print("页面返回信息：%s" % testData)
        #name = "D:\Work\Python\AutoTest\Report\测试报告20201215_104132.xlsx"
        #redict = dict(zip(["name", "method", "url", "result", "Response"],
        #                  ["这是条测试数据","post","www.baidu.com", "测试通过", "response"]))
        #re = writebook(name, redict)
        print("re返回：%s" )

if __name__ == '__main__':
    unittest.main()
