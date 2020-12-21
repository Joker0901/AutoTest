import ddt
import requests
import json
def gettoken():
  #print("开始")
  name = "登录获取token"
  url = "https://csppoc.fetiononline.com/api/sys/user/login"
  url1 = ''.join([url])
  method = "post"
  params = ""
  headers = "{'Content-Type':'application/json;charset=UTF-8'}"
  #用户名、密码可以替换自己想要的。
  body = "{'password':'123456','loginName':'admin','code':''}"
  type = "json"
  result = "\"code\":200"
  listApiData = []
  # 将数据放入到字典中
  mydict = dict(zip(["name", "url", "method", "params", "headers", "body", "type", "result"],[name, url, method, params, headers, body, type, result]))
  # 返回数据
  aa = eval(mydict['headers'])
  bb = json.dumps(eval(mydict['body']))
  re = requests.post(url1,headers = aa,data =bb,verify = False )
  r = re.json()
  data = r['data']
  accessToken = data['accessToken']
  accessToken = "access_token=" + accessToken

  print("获取token成功  {0}".format(accessToken) )

  return accessToken






