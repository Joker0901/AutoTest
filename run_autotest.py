__author__ = '优秀的北京团队'
import requests
import urllib3

from lib.comparison import comparison
from lib.readcase import readcase
from lib.readreport import  ReadReport
from lib.sendmail import send_mail
from lib.sendrequests import SendRequests
from lib.writreport import createbook, writebook

urllib3.disable_warnings()
testData = readcase()
print("生成测试用例数据成功：%s" % testData)
bookname = createbook()
print("bookname：%s" % bookname)

def run_case(casedata,reportpath):
    allcase = casedata
    name = reportpath
    for i in range(len(allcase)):
        case = allcase[i]
        print("第 {0} 条用例，用例名称： {1}".format(i+1,case['name']))
        # 发送请求
        print("****RUN****")
        s = requests.session()
        re = SendRequests().sendRequests(s, case)

        # 比对执行结果
        bl = comparison(case, re)
        # print ("执行结果123  ：%s" %result)
        print("预期结果  -->  {0}".format(case['result']))
        if bl:

            redict = dict(zip(["name", "method", "url", "result", "Response"],
                              [case['name'], case['method'], case['url'], "测试通过", re.content.decode("utf-8")]))
            reportbl = writebook(bookname, redict)
            print("测试报告： %s" % reportbl)

        else:

            redict = dict(zip(["name", "method", "url", "result", "Response"],
                              [case['name'], case['method'], case['url'], "测试通过", re.content.decode("utf-8")]))
            reportbl = writebook(bookname, redict)
            print("测试报告： %s" % reportbl)

    MailData = ReadReport(name).read_data() #读取执行结果
    send_mail(MailData)   #发送邮件

if __name__=='__main__':
    run_case(testData,bookname)