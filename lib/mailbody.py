from turtle import pd


def mailbody(testData):


    mail_data = testData
    d = ''
    for i in range(len(mail_data)):
        #print('打印下i = %s' %i)
        msg = mail_data[i]
        #print('打印下list = %s' %msg)
        d = d + """
             <tr>
                   <td align="center">""" + str(msg['ID']) + """</td>
                   <td>""" + msg['用例名称'] + """</td>
                   <td align="center">""" + msg['模式'] + """</td>
                   <td>""" + msg['URL'] + """</td>
                   <td  align="center">""" + msg['执行结果'] + """</td>
                 </tr>
                """

    html = """\
     <head>
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />


     <body>
     <div id="container">
     <p><strong>自建CSP平台测试结果:</strong></p>
     <div id="content">
      <table width="100%" border="2" bordercolor="black" cellspacing="0" cellpadding="0">
     <tr>
       <td width="100" align="center"><strong>ID</strong></td>
       <td width="100" align="center"><strong>用例名称</strong></td>
       <td width="100" align="center"><strong>模式</strong></td>
       <td width="100" align="center"><strong>URL</strong></td>
       <td width="100" align="center"><strong>执行结果</strong></td>
     </tr>""" + d + """
     </table>
     </div>
     </div>
     </div>
     </body>
     </html>
           """
    return html