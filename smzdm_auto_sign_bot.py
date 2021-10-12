"""
什么值得买自动签到脚本

借鉴（copy）自lws1122,fork 自:https://gitee.com/lsw1122/smzdm_bot
"""
'''
cron: 0 1 * * * smzdm_auto_sign_bot.py
new Env('张大妈自动签到');
'''

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

TG_TOKEN = ''
TG_USER_ID = ''

if "TG_BOT_TOKEN" in os.environ and len(os.environ["TG_BOT_TOKEN"]) > 1 and "TG_USER_ID" in os.environ and len(
        os.environ["TG_USER_ID"]) > 1:
    TG_TOKEN = os.environ["TG_BOT_TOKEN"]
    TG_USER_ID = os.environ["TG_USER_ID"]


def logout(self):
    print("[{0}]: {1}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self))
    sys.stdout.flush()


def loadSend():
    logout("加载ql自带的推送模块")
    global send
    send = None
    cur_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(cur_path)
    if os.path.exists(cur_path + "/sendNotify.py"):
        try:
            from sendNotify import send
            logout("加载ql自带的推送模块")
        except Exception as e:
            send = None
            logout("加载通知服务失败~", e)


def telegram_bot(title, content):
    try:
        print("\n")
        bot_token = TG_TOKEN
        user_id = TG_USER_ID
        if not bot_token or not user_id:
            print("tg服务的bot_token或者user_id未设置!!\n取消推送")
            return
        print("tg服务启动")
        url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'chat_id': str(TG_USER_ID), 'text': f'{title}\n\n{content}', 'disable_web_page_preview': 'true'}
        proxies = None

        try:
            response = requests.post(url=url, headers=headers, params=payload, proxies=proxies).json()
        except:
            print('推送失败！')
        if response['ok']:
            print('推送成功！')
        else:
            print('推送失败！')
    except Exception as e:
        print(e)


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
        msg = self.session.get(SIGN_URL)
        if self.__json_check(msg):
            return msg.json()
        return msg.content


if __name__ == '__main__':
    bot = SignBot()
    cookies = os.environ[KEY_OF_COOKIE]
    cookieList = cookies.split("&")
    logout("检测到{}个cookie记录\n开始签到".format(len(cookieList)))
    loadSend()
    index = 0
    for c in cookieList:
        bot.load_cookie_str(c)
        result = bot.checkin()
        msg = "\n⭐⭐⭐签到成功{1}天⭐⭐⭐\n🏅🏅🏅金币[{2}]\n🏅🏅🏅积分[{3}]\n🏅🏅🏅经验[{4}],\n🏅🏅🏅等级[{5}]\n🏅🏅补签卡[{6}]".format(
            index,
            result['data']["checkin_num"],
            result['data']["gold"],
            result['data']["point"],
            result['data']["exp"],
            result['data']["rank"],
            result['data']["cards"])
        logout(msg)
        if (send):
            send("张大妈自动签到", msg)
        else:
            logout("未注册推送，取消推送")
            # telegram_bot("张大妈自动签到", msg)
        index += 1
    logout("签到结束")
