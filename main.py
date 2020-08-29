#Author Atticus_lv
#-*- coding =utf-8 -*-
#@Time : 2020/8/29 14:57
#@File : main.py
#@Software : PyCharm

from WechatPCAPI import WechatPCAPI
import time
import logging
from queue import Queue

from spider import get_ele_info

#登录信息初始化
logging.basicConfig(level=logging.INFO)
queue_recved_message = Queue()


def on_message(message):
    queue_recved_message.put(message)


def deal_info():
    dict, time_str = get_ele_info()
    msg = time_str +"\n>>宿舍电量小助手<<"

    for key,value in dict.items():
        str = key + "：" + value
        msg = msg +"\n" + str
    return msg


def main():
    wx_inst = WechatPCAPI(on_message=on_message, log=logging)
    wx_inst.start_wechat(block=True)

    while not wx_inst.get_myself():
        time.sleep(5)

    print('登陆成功')
    print(wx_inst.get_myself())

    time.sleep(5)

    wx_inst.send_text(to_user='filehelper', msg='登录成功')

    msg = deal_info()
    # wx_inst.send_text(to_user='filehelper', msg=msg)
    wx_inst.send_text(to_user='22893751767@chatroom', msg=msg)


if __name__ == '__main__':
    main()