# _*_ coding:utf-8 _*_
import os, sys
import time

from lib.mailbody import mailbody

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(testData):
    """
    定义发送邮件
    :param file_new:
    :return: 成功：打印发送邮箱成功；失败：返回失败信息
    """
    #f = open(file_new, 'rb')

    mail_body = mailbody(testData)
    #f.close()
    # 发送附件
    localtime = time.strftime('%Y%m%d_%H%M', time.localtime(time.time()))
    #report = new_report(setting.TEST_REPORT)
    #sendfile = open(report, 'rb').read()
    # --------- 读取config.ini配置文件 ---------------
    SENDER = 'mazhenxin@feinno.com'
    RECEIVER = 'mazhenxin@feinno.com'
    USER = 'mazhenxin@feinno.com'
    PWD = 'ma19820415'
    SUBJECT = "自建CSP平台自动化测试结果%s"%localtime

    #att = MIMEText(mail_body, 'base64', 'utf-8')
    #att["Content-Type"] = 'application/octet-stream'
    #att.add_header("Content-Disposition", "attachment", filename=("gbk", "", report))

    msg = MIMEMultipart('related')
    #msg.attach(att)
    msgtext = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msgtext)
    msg['Subject'] = SUBJECT
    msg['from'] = SENDER
    msg['to'] = RECEIVER
    msg1 =msg.as_string()

    try:
        server = smtplib.SMTP()
        server.connect('smtp.feinno.com',587)
        #server.starttls()
        server.login(USER, PWD)
        server.sendmail(SENDER, RECEIVER, msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as  e:
        print("失败: " + str(e))


