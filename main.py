"""
什么值得买自动签到脚本
使用github actions 定时执行
@author : stark
"""
import requests,os
from sys import argv

 

"""
请求头
"""
DEFAULT_HEADERS = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'zhiyou.smzdm.com',
        'Referer': 'https://www.smzdm.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        }


"""
调试用 COOKIE
"""
TEST_COOKIE = ''


"""
调试用 SERVERCHAN_SECRETKEY
"""
SERVERCHAN_SECRETKEY = ''

class SMZDM_Bot(object):
    def __init__(self):
        self.session = requests.Session()
        # 添加 headers
        self.session.headers = DEFAULT_HEADERS

    def __json_check(self, msg):
        """
        对请求 盖乐世社区 返回的数据进行进行检查
        1.判断是否 json 形式
        """
        try:
            result = msg.json()
            print(result)
            return True
        except Exception as e:
            print(f'Error : {e}')            
            return False

    def load_cookie_str(self, cookies):
        """
        起一个什么值得买的，带cookie的session
        cookie 为浏览器复制来的字符串
        :param cookie: 登录过的社区网站 cookie
        """
        self.session.headers['Cookie'] = cookies    

    def checkin(self):
        """
        签到函数
        """
        url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
        msg = self.session.get(url)
        if self.__json_check(msg):
            return msg.json()
        return msg.content




if __name__ == '__main__':
    sb = SMZDM_Bot()
    # sb.load_cookie_str(config.TEST_COOKIE)
    cookies = "r_sort_type=score; __ckguid=N6SifpT6HxsNjjKueY4hJ2; __jsluid_s=b2080c425b81b90a001eb589a86d934d; smzdm_user_source=B1C59A78112612FCAD7D2132E0D42EDB; shequ_pc_sug=b; _ga_271744817=GS1.1.1620712436.1.1.1620712656.0; device_id=173711656516269218482803068eabb31532836e8b33c28a25b4925adb; _gid=GA1.2.606015419.1629253607; zdm_qd=%7B%22referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D1Cal19BBPzHR5TmG_ak5FO4792JG6e9T3AjbqVeKdgsAhqZcDbEDVXMkWAxaAmSp%26wd%3D%26eqid%3D9a64efa200013fb700000005611cadce%22%7D; homepage_sug=e; _gat_UA-27058866-1=1; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1626748610,1627027147,1629272705; sess=AT-mnKeYzZwNdGQZ1bUniDitWGgFdF6LgBcQw5bpJUENyNWrkTDuHweoEPb8Y5Qs4rWGgf3JQizwwmwlT8zgMkWusOD0WtrnXQBf8Pf5NrV84Tc8XFSxsUtVvwP; user=timblack%7C6769336630; _zdmA.uid=ZDMA.6Xz2C1CBX.1629272735.2419200; smzdm_id=6769336630; __gads=ID=d319c1b0be6953a5:T=1615454974:S=ALNI_MbKON5Brm3uPlXWLH2oUJ-ohJH5hA; smzdm_user_view=6C64243AD38F31CF88181A8D484FB74C; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%226769336630%22%2C%22first_id%22%3A%22174493ade544c0-0ea30d6db9c2ac-4e4c0f20-2073600-174493ade55638%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22174493ade544c0-0ea30d6db9c2ac-4e4c0f20-2073600-174493ade55638%22%7D; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1629272759; _ga_09SRZM2FDD=GS1.1.1629272703.20.1.1629272759.0; _ga=GA1.1.774295214.1564131947"
    sb.load_cookie_str(cookies)
    res = sb.checkin()
    print(res)
    SERVERCHAN_SECRETKEY = os.environ["SERVERCHAN_SECRETKEY"]
    print('sc_key: ', SERVERCHAN_SECRETKEY)
    if isinstance(SERVERCHAN_SECRETKEY,str) and len(SERVERCHAN_SECRETKEY)>0:
        print('检测到 SCKEY， 准备推送')
       
    print('代码完毕')