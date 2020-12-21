#登录获取token
#对有“的字符串，需要在符号前加入\进行转义

class TestCase1():
  def login(self):
        name = "登录获取token"
        url = "https://csppoc.fetiononline.com/api/sys/user/login"
        method = "post"
        params = ""
        headers = "{'Content-Type':'application/json;charset=UTF-8'}"
        body = "{'password':'123456','loginName':'admin','code':''}"
        type = "json"
        result = "\"code\":200"
        listApiData = []
        # 将数据放入到字典中
        api_dict = dict(zip(["name", "url", "method", "params", "headers", "body", "type", "result"],[name, url, method, params, headers, body, type, result]))
        # 返回数据
        listApiData.append(api_dict)
        return listApiData

  #查询敏感词列表
  def searchwords(self,token):
      token = token
      name = "搜索敏感词列表"
      url = "https://csppoc.fetiononline.com/api/taboo/page?pageSize=10&pageNumber=1"
      method = "post"
      params = ""
      headers = "{'Content-Type':'application/json;charset=UTF-8','Cookie':'%s'}" %token
      body = "{}"
      type = "json"
      result = "\"code\":200"
      listApiData = []
      # 将数据放入到字典中
      api_dict = dict(zip(["name", "url", "method", "params", "headers", "body", "type", "result"],[name, url, method, params, headers, body, type, result]))
      # 返回数据
      listApiData.append(api_dict)
      return listApiData

  # 获取用户列表
  def userlist(self,token):
      token = token
      name = "获取用户列表"
      url = "https://csppoc.fetiononline.com/api/channelUser/userLabelList?channelId=533954155098669056"
      method = "get"
      params = ""
      headers = "{'Content-Type':'application/json;charset=UTF-8','Cookie':'%s'}" %token
      body = ""
      type = "data"
      result ="\"code\":200"
      listApiData = []
      # 将数据放入到字典中
      api_dict = dict(zip(["name", "url", "method", "params", "headers", "body", "type", "result"],[name, url, method, params, headers, body, type, result]))
      # 返回数据
      listApiData.append(api_dict)
      return listApiData

  # 获取首页信息
  def firstpage(self, token):
      token = token
      name = "获取首页信息"
      url = "https://csppoc.fetiononline.com/api/channel/page?pageSize=10&pageNumber=1"
      method = "post"
      params = ""
      headers = "{'Content-Type':'application/json;charset=UTF-8','Cookie':'%s'}" % token
      body = "{}"
      type = "json"
      result = "\"code\":200"
      listApiData = []
      # 将数据放入到字典中
      api_dict = dict(zip(["name", "url", "method", "params", "headers", "body", "type", "result"],
                          [name, url, method, params, headers, body, type, result]))
      # 返回数据
      listApiData.append(api_dict)
      return listApiData