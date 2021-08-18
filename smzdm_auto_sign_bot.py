"""
什么值得买自动签到脚本

借鉴（copy）自lws1122,fork 自:https://gitee.com/lsw1122/smzdm_bot
"""
import requests, os, datetime, sys
from sys import argv

"""
http headers
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

# 签到用的url
SIGN_URL = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'

# 环境变量中用于存放cookie的key值
KEY_OF_COOKIE = "SMZDM_COOKIE"


def logout(self):
    print("[{0}]: {1}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self))
    sys.stdout.flush()


class SignBot(object):

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
            logout(result)
            return True
        except Exception as e:
            logout(f'Error : {e}')
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
        logout("开始签到")
        msg = self.session.get(SIGN_URL)
        if self.__json_check(msg):
            return msg.json()
        return msg.content


if __name__ == '__main__':
    bot = SignBot()
    cookies = os.environ[KEY_OF_COOKIE]
    bot.load_cookie_str(cookies)
    res = bot.checkin()
    logout(res)
    logout("签到结束")
