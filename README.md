什么值得买每日签到脚本 
===
 
    <img src="https://img.shields.io/badge/Created on-2021.8-green"/>
    <img src="https://img.shields.io/badge/Python-3.7-blue"/>
    <img src="https://img.shields.io/badge/Last commit-Aut.-yellow"/>
    <img src="https://img.shields.io/badge/Repo size-35.8kb-red"/>
 

 

## 声明
 + 借鉴(chao) 自 [lsw1122](https://gitee.com/lsw1122) 的开源项目:[什么值得买每日签到脚本](https://gitee.com/lsw1122/smzdm_bot)
 + 原作者似乎很久没维护了，所以为了自己使用方便，在其基础上集成了青龙面板的逻辑
 + server酱最近相当不稳定，而且似乎公众号推送后期将废弃，所以把原来里面的逻辑去掉了
 + 因为python仅仅是略懂，所以然后又借鉴(chao) 了 [faker2](https://github.com/shufflewzc/faker2) 里的一些代码，把telegram推送集成了一下
 + 综上自己可以用的很爽了。彻底解放双手




# 1. 实现功能

+ [什么值得买](https://www.smzdm.com) 每日签到
+ 通过telegram推送签到结果
+ 可通过青龙面板拉取最新逻辑每日1点(默认)定时运行
+ 支持配置多个账号一起签到

# 2. 使用方法
1. 搭配青龙面板使用
2. 面板中定时任务-添加任务-新增定时 `ql repo https://github.com/sunflo/smzdm_sign_bot.git`
3. 面板环境变量中添加，smzdm的cookie信息，key值必须是`SMZDM_COOKIE`
4. 需要实现电报推送的，通过面板-配置文件添加`TG_BOT_TOKEN`及`TG_USER_ID`

